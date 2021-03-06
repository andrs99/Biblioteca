# Generated by Django 3.0 on 2020-03-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo_nombre', models.CharField(max_length=30)),
                ('articulo_seccion', models.CharField(max_length=30)),
                ('articulo_precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nombre', models.CharField(max_length=50)),
                ('cliente_email', models.EmailField(max_length=254)),
                ('cliente_direccion', models.CharField(max_length=50)),
                ('cliente_telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_numero', models.IntegerField()),
                ('pedido_fecha', models.DateField()),
                ('pedido_entregado', models.BooleanField()),
            ],
        ),
    ]
