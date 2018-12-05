# Generated by Django 2.1.4 on 2018-12-05 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('codigo_lista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_lista', models.CharField(max_length=30)),
                ('codigo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=30)),
                ('costo_presupuestado', models.IntegerField(blank=True, null=True)),
                ('costo_real', models.IntegerField(blank=True, null=True)),
                ('notas', models.CharField(blank=True, max_length=30, null=True)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backEnd.Lista')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('codigo_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tienda', models.CharField(max_length=30)),
                ('nombre_sucursal', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion', models.CharField(max_length=40)),
                ('region', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backEnd.Tienda'),
        ),
    ]
