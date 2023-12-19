# Generated by Django 4.2.4 on 2023-08-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idusuario', models.CharField(db_column='IDUsuario', max_length=16)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('clave', models.CharField(max_length=32)),
                ('fechacreacion', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
                ('tipousuario', models.CharField(db_column='TipoUsuario', max_length=8)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]
