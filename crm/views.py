from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Cliente  # Asegúrate de importar el modelo Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile_view(request):
    return redirect('/admin/')  # Redirige directamente a la URL del admin

# @login_required
# def lista_clientes(request):
#     # Redirige a la URL de administración de clientes
#     return redirect('/admin/crm/cliente/')

# @login_required
# def lista_clientes(request):
#     clientes = Cliente.objects.all()
#     return render(request, 'lista_clientes.html', {'clientes': clientes, 'request': request})

@login_required
def lista_clientes(request):
    query = request.GET.get('q', '')  # Recoge el término de búsqueda del parámetro 'q'
    if query:
        # Filtra clientes por nombre o email usando el término de búsqueda
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(email__icontains=query)
        )
    else:
        # Si no hay término de búsqueda, muestra todos los clientes
        clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes, 'query': query})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el cliente en la base de datos
            messages.success(request, "Cliente agregado exitosamente.")
            return redirect('lista_clientes')  # Redirige a la lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'add_cliente.html', {'form': form})

@login_required
@permission_required('crm', raise_exception=True)
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente.')
    return redirect('lista_clientes')  # Redirige a la lista de clientes