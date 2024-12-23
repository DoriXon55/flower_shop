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
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Colors(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'colors'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    delivery_data = models.DateField(blank=True, null=True)
    delivery_name = models.ForeignKey('Deliveryname', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Deliveryname(models.Model):
    delivery_name_id = models.IntegerField(primary_key=True)
    firm_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliveryname'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Firm(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nip = models.CharField(db_column='NIP', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firm'


class Flower(models.Model):
    flower_id = models.IntegerField(primary_key=True)
    flower_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower'


class Flowercolors(models.Model):
    flower = models.OneToOneField(Flower, models.DO_NOTHING,
                                  primary_key=True)  # The composite primary key (flower_id, color_id) found, that is not supported. The first column is selected.
    color = models.ForeignKey(Colors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flowercolors'
        unique_together = (('flower', 'color'),)


class Individual(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True)
    individual_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'individual'


class Orderflower(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING,
                                 primary_key=True)  # The composite primary key (order_id, flower_id) found, that is not supported. The first column is selected.
    flower = models.ForeignKey(Flower, models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderflower'
        unique_together = (('order', 'flower'),)


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    total_amount = models.FloatField()
    order_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey('Paymenttype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Paymenttype(models.Model):
    payment_type_id = models.IntegerField(primary_key=True)
    payment_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymenttype'


class ShopAppColor(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shop_app_color'


class ShopAppCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_customer'


class ShopAppDelivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    delivery_data = models.DateField(blank=True, null=True)
    delivery_name = models.ForeignKey('ShopAppDeliveryname', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('ShopAppStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_delivery'


class ShopAppDeliveryname(models.Model):
    delivery_name_id = models.AutoField(primary_key=True)
    firm_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_deliveryname'


class ShopAppEmployee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_employee'


class ShopAppFirm(models.Model):
    customer = models.OneToOneField(ShopAppCustomer, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nip = models.CharField(db_column='NIP', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shop_app_firm'


class ShopAppFlower(models.Model):
    flower_id = models.AutoField(primary_key=True)
    flower_name = models.CharField(max_length=50)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'shop_app_flower'


class ShopAppFlowercolor(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.ForeignKey(ShopAppColor, models.DO_NOTHING)
    flower = models.ForeignKey(ShopAppFlower, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_app_flowercolor'
        unique_together = (('flower', 'color'),)


class ShopAppIndividual(models.Model):
    customer = models.OneToOneField(ShopAppCustomer, models.DO_NOTHING, primary_key=True)
    individual_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_individual'


class ShopAppOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    total_amount = models.FloatField()
    order_date = models.DateTimeField()
    customer = models.ForeignKey(ShopAppCustomer, models.DO_NOTHING, blank=True, null=True)
    delivery = models.ForeignKey(ShopAppDelivery, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(ShopAppEmployee, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey('ShopAppPaymenttype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_order'


class ShopAppOrderflower(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    flower = models.ForeignKey(ShopAppFlower, models.DO_NOTHING)
    order = models.ForeignKey(ShopAppOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_app_orderflower'
        unique_together = (('order', 'flower'),)


class ShopAppPaymenttype(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_paymenttype'


class ShopAppStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_app_status'


class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'
