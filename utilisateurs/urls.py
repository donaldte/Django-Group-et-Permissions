from django.urls import path

from utilisateurs.views import addToPremiumGroup

urlpatterns = [
    path('addtopremuim', addToPremiumGroup, name='addtopremuin'),
]
