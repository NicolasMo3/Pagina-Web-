# Generated by Django 4.2.16 on 2024-11-08 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0005_cliente_empresa"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="estado",
            field=models.CharField(
                choices=[
                    ("Nuevo", "Nuevo"),
                    ("Proceso", "Proceso"),
                    ("Contactado", "Contactado"),
                    ("Laboratorio", "Laboratorio"),
                    ("Trabajo", "Trabajo"),
                ],
                default="",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="cliente",
            name="fecha_in",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Fecha de Ingreso"
            ),
        ),
        migrations.AddField(
            model_name="cliente",
            name="fecha_sal",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Fecha de Salida"
            ),
        ),
        migrations.AddField(
            model_name="cliente",
            name="observacion",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="operario",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="sucursal",
            field=models.CharField(
                choices=[
                    ("Barranquilla", "Barranquilla"),
                    ("Bucaramanga", "Bucaramanga"),
                    ("Cali", "Cali"),
                    ("Centro", "Centro"),
                    ("Chapinero", "Chapinero"),
                    ("Chía", "Chía"),
                    ("Cúcuta", "Cúcuta"),
                    ("Deposito", "Deposito"),
                    ("Manizales", "Manizales"),
                    ("Medellín", "Medellín"),
                    ("Neiva", "Neiva"),
                    ("Olaya", "Olaya"),
                    ("Pereira", "Pereira"),
                    ("Pincipal", "Pincipal"),
                    ("PteAranda", "PteAranda"),
                    ("Rio Negro", "Rio Negro"),
                    ("Tunja", "Tunja"),
                ],
                default="",
                max_length=32,
            ),
        ),
    ]
