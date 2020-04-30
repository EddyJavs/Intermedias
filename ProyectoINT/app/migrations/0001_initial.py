# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('nit', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=150)),
                ('sede', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.CharField(primary_key=True, max_length=150, serialize=False)),
                ('codigoBarras', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('categoria', models.ManyToManyField(to='app.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('alias', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=150)),
                ('municipio', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dpi', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('encargado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_facturacion', models.DateField()),
                ('fecha_entrega', models.DateField(null=True)),
                ('cliente', models.ForeignKey(to='app.Cliente')),
                ('vendedor', models.ForeignKey(to='app.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Venta_Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(to='app.Producto')),
                ('id_venta', models.ForeignKey(to='app.Venta')),
            ],
        ),
        migrations.AddField(
            model_name='sede',
            name='enargado',
            field=models.ForeignKey(db_column='dpi', to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='encargado',
            field=models.ForeignKey(db_column='dpi', to='app.Usuario'),
        ),
    ]
