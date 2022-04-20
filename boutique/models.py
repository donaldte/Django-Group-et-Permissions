from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=15)
    image = models.ImageField(upload_to = "productimages", default = None, null = True, blank = True)
    price = models.FloatField()
    brand = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)

# ............Cette methode fonction dans le terminal

# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# ct = ContentType.objects.get_for_model(Product)
# permission = Permission.objects.create(codename='can_do_this', contentype=ct)


class PremiumProduct(models.Model):
    product_name = models.CharField(max_length=15)
    image = models.ImageField(upload_to = "firstapp/premiumproductimages", default = None, null = True, blank = True)
    price = models.FloatField()
    brand = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)

    # # custom permissions dependent to a specific model
    class Meta:
        permissions = (
            ('can_see_command_premuin', 'can see command for premium delivery on premium products'),
            ('can_add_premium_discount', 'can avail more premium discount on premium products')
       )



class CustomPermissions(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion  \
                         # operations will be performed for this model.

        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        # All the custom permissions not related to models on Manufacturer
        permissions = (
            ('accept_order', 'can accept order'),
            ('reject_order', 'can reject order'),
            ('view_order', 'can view order'),
            ('change_order', 'can change order'),
            ('view_return', 'can view return'),
            ('accept_return', 'can accept return'),
            ('reject_return', 'can reject return'),
            ('change_return', 'can change return'),
            ('view_dashboard', 'can view dashboard'),
        )