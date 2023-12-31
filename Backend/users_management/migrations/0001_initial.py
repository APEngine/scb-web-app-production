# Generated by Django 4.1 on 2023-12-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users_management_auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_management_auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_management_auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'users_management_auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'users_management_django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users_management_django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_management_django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_management_django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horasdedicadastareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoproyecto', models.CharField(db_column='CodigoProyecto', max_length=10)),
                ('codigotarea', models.CharField(blank=True, db_column='CodigoTarea', max_length=10, null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=250, null=True)),
                ('horasdedicadas', models.FloatField(blank=True, db_column='HorasDedicadas', null=True)),
                ('fechacreacion', models.DateTimeField()),
                ('aprobadas', models.IntegerField(blank=True, db_column='Aprobadas', null=True)),
            ],
            options={
                'db_table': 'users_management_horasdedicadastareas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoproyecto', models.CharField(db_column='CodigoProyecto', max_length=10)),
                ('codigocliente', models.CharField(blank=True, db_column='codigoCliente', max_length=8, null=True)),
                ('tipoproyecto', models.CharField(db_column='TipoProyecto', max_length=5)),
                ('programador', models.CharField(blank=True, db_column='Programador', max_length=8, null=True)),
                ('administrador', models.CharField(db_column='Administrador', max_length=8)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=250, null=True)),
                ('horasproyectadas', models.IntegerField(blank=True, db_column='HorasProyectadas', null=True)),
                ('fechacreacion', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_management_proyectos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoproyecto', models.CharField(db_column='CodigoProyecto', max_length=10)),
                ('codigotarea', models.CharField(db_column='CodigoTarea', max_length=10)),
                ('programador', models.CharField(db_column='Programador', max_length=8)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=250, null=True)),
                ('horasproyectadas', models.FloatField(blank=True, db_column='HorasProyectadas', null=True)),
                ('fechacreacion', models.DateTimeField()),
                ('aprobada', models.IntegerField(blank=True, db_column='Aprobada', null=True)),
                ('fechaaprobacion', models.DateTimeField(blank=True, null=True)),
                ('prioridad', models.IntegerField()),
            ],
            options={
                'db_table': 'users_management_tareas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipousuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtipousuario', models.IntegerField(db_column='idTipoUsuario')),
                ('tipo', models.CharField(db_column='Tipo', max_length=15)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=50)),
            ],
            options={
                'db_table': 'users_management_tipousuarios',
                'managed': False,
            },
        ),
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
                'db_table': 'users_management_usuarios',
                'managed': False,
            },
        ),
    ]
