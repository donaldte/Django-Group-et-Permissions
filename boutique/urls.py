from django.urls import path
from boutique import views

app_name = 'boutique'
urlpatterns = [
    #path('', views.store, name='store'),
    path('', views.StoreView.as_view(), name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]
