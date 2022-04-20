# Generated by Django 4.0.4 on 2022-04-20 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_premiumproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('accept_order', 'can accept order'), ('reject_order', 'can reject order'), ('view_order', 'can view order'), ('change_order', 'can change order'), ('view_return', 'can view return'), ('accept_return', 'can accept return'), ('reject_return', 'can reject return'), ('change_return', 'can change return'), ('view_dashboard', 'can view dashboard')),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]