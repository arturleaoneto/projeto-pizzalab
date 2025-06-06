# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey("Pedido", models.DO_NOTHING, db_column="id_pedido")
    id_cliente = models.ForeignKey(
        "Pedido",
        models.DO_NOTHING,
        db_column="id_cliente",
        related_name="avaliacao_id_cliente_set",
    )
    nota_pizza = models.IntegerField()
    nota_atendimento = models.IntegerField()
    data_avaliacao = models.DateField()
    comentario = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = "avaliacao"


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=60, blank=True, null=True)
    rua = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cliente"


class Compraingrediente(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_fornecedor = models.ForeignKey(
        "Fornecedor", models.DO_NOTHING, db_column="id_fornecedor"
    )
    id_ingrediente = models.ForeignKey(
        "Ingrediente", models.DO_NOTHING, db_column="id_ingrediente"
    )
    cnpj = models.CharField(max_length=30, blank=True, null=True)
    datacompra = models.DateField()
    valor_ingrediente = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "compraingrediente"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey("UserProfile", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey("Pedido", models.DO_NOTHING, db_column="id_pedido")
    data_entrega = models.DateTimeField(blank=True, null=True)
    id_funcionario = models.IntegerField()
    situacao_entrega = models.CharField(max_length=30, blank=True, null=True)
    endereco_entrega = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "entrega"


class Escalatrabalho(models.Model):
    id_escala = models.AutoField(primary_key=True)
    id_funcionario = models.ForeignKey(
        "Funcionario", models.DO_NOTHING, db_column="id_funcionario"
    )
    data_escala = models.DateField()
    tipo_turno = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = "escalatrabalho"


class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True, null=True)
    cnpj = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fornecedor"


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    salario = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "funcionario"


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    medida = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    un_medida = models.CharField(max_length=30, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ingrediente"


class ItensPedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_pizza = models.ForeignKey(
        "Pizza", models.DO_NOTHING, db_column="id_pizza", blank=True, null=True
    )
    quantidade = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "itens_pedido"


class LogPizza(models.Model):
    id_log = models.AutoField(primary_key=True)
    quantidade_pizzas = models.IntegerField(blank=True, null=True)
    data_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "log_pizza"


class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(
        "Pedido", models.DO_NOTHING, db_column="id_pedido", blank=True, null=True
    )
    data_pagamento = models.DateTimeField(blank=True, null=True)
    forma_pagamento = models.CharField(max_length=30, blank=True, null=True)
    valor_pago = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "pagamento"


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column="id_cliente", blank=True, null=True
    )
    data_pedido = models.DateTimeField(blank=True, null=True)
    situacao = models.CharField(max_length=30, blank=True, null=True)
    endereco_entrega = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pedido"


class Pizza(models.Model):
    id_pizza = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    id_tipo = models.ForeignKey(
        "TipoPizza", models.DO_NOTHING, db_column="id_tipo", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "pizza"


class PizzaIngrediente(models.Model):
    id_pizza = models.IntegerField()
    id_ingrediente = models.ForeignKey(
        Ingrediente,
        models.DO_NOTHING,
        db_column="id_ingrediente",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "pizza_ingrediente"


class Promocao(models.Model):
    id_promocao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    desconto = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    data_inicio = models.DateTimeField(blank=True, null=True)
    data_fim = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "promocao"


class TamanhoPizza(models.Model):
    id_tamanho = models.AutoField(primary_key=True)
    tamanho = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tamanho_pizza"


class TipoPizza(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tipo_pizza"


class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=False, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=133)
    cpf = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = "user_profile"


class UserProfileGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(UserProfile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "user_profile_groups"
        unique_together = (("profile", "group"),)


class UserProfileUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile = models.ForeignKey(UserProfile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "user_profile_user_permissions"
        unique_together = (("profile", "permission"),)


class ValorPizza(models.Model):
    id_valor = models.AutoField(primary_key=True)
    id_tamanho = models.ForeignKey(
        TamanhoPizza, models.DO_NOTHING, db_column="id_tamanho"
    )
    id_tipo = models.ForeignKey(TipoPizza, models.DO_NOTHING, db_column="id_tipo")
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "valor_pizza"
