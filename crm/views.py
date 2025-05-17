from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Cliente  # Asegúrate de importar el modelo Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import PerfilUsuario
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile_view(request):
    return redirect('/admin/')  # Redirige directamente a la URL del admin


# @login_required
# def lista_clientes(request):
#     query = request.GET.get('q', '')  # Recoge el término de búsqueda del parámetro 'q'
#     if query:
#         # Filtra clientes por nombre o email usando el término de búsqueda
#         clientes = Cliente.objects.filter(
#             Q(cliente__icontains=query) | Q(email__icontains=query)
#         )
#     else:
#         # Si no hay término de búsqueda, muestra todos los clientes
#         clientes = Cliente.objects.all()
#     return render(request, 'lista_clientes.html', {'clientes': clientes, 'query': query})

def lista_clientes(request):
    query = request.GET.get('q', '')
    empresa = request.GET.get('empresa', '')
    fecha_in = request.GET.get('fecha_in', '')
    # fecha_sal = request.GET.get('fecha_sal', '')
    sucursal = request.GET.get('sucursal', '')
    asesor = request.GET.get('asesor', '')

    # Filtrado de los clientes según los parámetros
    clientes = Cliente.objects.all()
    if query:
        clientes = clientes.filter(nombre__icontains=query)

    if empresa:
        clientes = clientes.filter(empresa__icontains=empresa)

    if sucursal:
        clientes = clientes.filter(sucursal=sucursal)

    if asesor:
        clientes = clientes.filter(asesor=asesor)

    # Filtro de fecha de ingreso (fecha_in)
    if fecha_in:
        try:
            # Solo convierte si fecha_in tiene un valor
            fecha_in_obj = datetime.strptime(fecha_in, "%Y-%m-%d").date()
            clientes = clientes.filter(fecha_in__gte=fecha_in_obj)  # Filtra desde la fecha de ingreso
        except ValueError:
            pass  # Si la fecha no es válida, no hace nada

    # Filtro de fecha de salida (fecha_sal)
    # if fecha_sal:
    #     try:
    #         # Solo convierte si fecha_sal tiene un valor
    #         fecha_sal_obj = datetime.strptime(fecha_sal, "%Y-%m-%d").date()
    #         clientes = clientes.filter(fecha_sal__lte=fecha_sal_obj)  # Filtra hasta la fecha de salida
    #     except ValueError:
    #         pass  # Si la fecha no es válida, no hace nada

    # Pasar los valores de filtro al template
    return render(request, 'lista_clientes.html', {
        'clientes': clientes,
        'query': query,
        'query_empresa': empresa,
        'query_fecha_in': fecha_in,
        # 'query_fecha_sal': fecha_sal,
        'query_sucursal': sucursal,
        'query_asesor': asesor,
        'empresas': Cliente.objects.values_list('empresa', flat=True).distinct(),
        'sucursales': Cliente.objects.values_list('sucursal', flat=True).distinct(),
        'asesores': Cliente.objects.values_list('asesor', flat=True).distinct(),
    })

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_cliente(request):
    try:
        if request.method == "POST":
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()  # Guarda el cliente en la base de datos
                messages.success(request, "Cliente agregado exitosamente.")
                form = ClienteForm()
                # return redirect('lista_clientes')  # Redirige a la lista de clientes
        else:
            form = ClienteForm()
        return render(request, 'add_cliente.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"Error: {e}")

@login_required
@permission_required('crm', raise_exception=True)
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente.')
    return redirect('lista_clientes')  # Redirige a la lista de clientes


def encuesta(request):
    encuesta_script = None

    if request.user.is_authenticated:
        try:
            perfil = PerfilUsuario.objects.get(user=request.user)
            encuesta_script = perfil.encuesta_script  # Obtener el script de la base de datos
        except PerfilUsuario.DoesNotExist:
            pass  # Si el usuario no tiene encuesta asignada, se deja vacío

    return render(request, 'encuesta.html', {'encuesta_script': encuesta_script})