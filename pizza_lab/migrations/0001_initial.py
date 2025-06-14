# Generated by Django 4.2.21 on 2025-05-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("id_cliente", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=30)),
                ("data_nascimento", models.DateField(blank=True, null=True)),
                ("sexo", models.CharField(blank=True, max_length=1, null=True)),
                ("telefone", models.CharField(max_length=15)),
                ("email", models.CharField(blank=True, max_length=60, null=True)),
                ("rua", models.CharField(blank=True, max_length=30, null=True)),
                ("numero", models.CharField(blank=True, max_length=15, null=True)),
                ("bairro", models.CharField(blank=True, max_length=30, null=True)),
                ("complemento", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "cliente",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Entrega",
            fields=[
                ("id_entrega", models.AutoField(primary_key=True, serialize=False)),
                ("id_pedido", models.IntegerField()),
                ("data_entrega", models.DateTimeField(blank=True, null=True)),
                ("id_funcionario", models.IntegerField()),
                (
                    "situacao_entrega",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "endereco_entrega",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
            ],
            options={
                "db_table": "entrega",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                ("id_funcionario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=30)),
                ("cargo", models.CharField(blank=True, max_length=30, null=True)),
                ("telefone", models.CharField(blank=True, max_length=11, null=True)),
                (
                    "salario",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
            options={
                "db_table": "funcionario",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ingrediente",
            fields=[
                ("id_ingrediente", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=30)),
                ("descricao", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "medida",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                ("un_medida", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
            ],
            options={
                "db_table": "ingrediente",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ItensPedido",
            fields=[
                ("id_pedido", models.AutoField(primary_key=True, serialize=False)),
                ("id_pizza", models.IntegerField(blank=True, null=True)),
                (
                    "quantidade",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
            ],
            options={
                "db_table": "itens_pedido",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LogPizza",
            fields=[
                ("id_log", models.AutoField(primary_key=True, serialize=False)),
                ("quantidade_pizzas", models.IntegerField(blank=True, null=True)),
                ("data_registro", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "log_pizza",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pagamento",
            fields=[
                ("id_pagamento", models.AutoField(primary_key=True, serialize=False)),
                ("id_pedido", models.IntegerField(blank=True, null=True)),
                ("data_pagamento", models.DateTimeField(blank=True, null=True)),
                (
                    "forma_pagamento",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "valor_pago",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
            ],
            options={
                "db_table": "pagamento",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                ("id_pedido", models.AutoField(primary_key=True, serialize=False)),
                ("id_cliente", models.IntegerField(blank=True, null=True)),
                ("data_pedido", models.DateTimeField(blank=True, null=True)),
                ("situacao", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "endereco_entrega",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "db_table": "pedido",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                ("id_pizza", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=60)),
                ("descricao", models.CharField(blank=True, max_length=150, null=True)),
                ("tamanho", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("tipo", models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                "db_table": "pizza",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PizzaIngrediente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_pizza", models.IntegerField()),
                ("id_ingrediente", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "pizza_ingrediente",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Promocao",
            fields=[
                ("id_promocao", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=60)),
                ("descricao", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "desconto",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("data_inicio", models.DateTimeField(blank=True, null=True)),
                ("data_fim", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "promocao",
                "managed": False,
            },
        ),
    ]
