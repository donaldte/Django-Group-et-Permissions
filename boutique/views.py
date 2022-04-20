from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from boutique.models import Product
from .mixins import CheckPremiumGroupMixin

# Create your views here.
from .decorators import group_required

# @group_required('premium')
# def store(request):
#     #if request.user.groups.filter(name='premium').exists():
    #return render(request, 'boutique/store.html')
#     #else:
#         #return HttpResponse('<h1> Vous n\'avez pas access au produits premium </h1>')  
#   
# class StoreView(CheckPremiumGroupMixin, ListView):
#     model = Product
#     template_name = 'boutique/store.html'

def cart(request):
    return render(request, 'boutique/cart.html')

def checkout(request):
    return render(request, 'boutique/checkout.html') 

from django.contrib.auth.decorators import permission_required

# @permission_required('boutique.view_product')
# def store(request):
#     # return render(request, 'boutique/store.html')


# #     # ctype = ContentType.objects.get_for_model(Product)
# #     # if request.user.permissions.filter(codename='view_product', contentype=ctype).exists():
#     if request.user.has_perm('boutique.view_product'):
#         return render(request, 'boutique/store.html')
#     else:
#         return HttpResponse('<h1> vous n\'avez pas access')    

from django.contrib.auth.mixins import PermissionRequiredMixin

class StoreView(PermissionRequiredMixin,  ListView):
    template_name = 'boutique/store.html'
    model = Product
    permission_required = 'boutique.view_product'        
    