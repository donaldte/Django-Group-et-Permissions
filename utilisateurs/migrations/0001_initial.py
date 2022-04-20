# Generated by Django 4.0.4 on 2022-04-19 22:29

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import multiselectfield.db.fields
import utilisateurs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', utilisateurs.models.LowercaseEmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Seller', 'SELLER'), ('Customer', 'CUSTOMER')], default=[], max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Ready For Shipment'), (3, 'Shipped'), (4, 'Delivered')], default=1)),
                ('total_amount', models.FloatField()),
                ('payment_status', models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3)),
                ('order_id', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('datetime_of_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=500, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='otp should be in six digits', regex='^\\d{6}$')])),
                ('phone', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('expiry', models.DateTimeField(default=datetime.datetime(2022, 4, 19, 22, 34, 29, 53615, tzinfo=utc))),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='firstapp/productimages')),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SellerAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst', models.CharField(max_length=10)),
                ('warehouse_location', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_name', models.CharField(max_length=255)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('utilisateurs.customuser',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('utilisateurs.customuser',),
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('product_in_cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.product')),
            ],
            options={
                'unique_together': {('cart', 'product')},
            },
        ),
    ]
