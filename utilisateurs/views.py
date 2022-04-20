from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def addToPremiumGroup(request):
    group = Group.objects.get(name='premium')
    request.user.groups.add(group)
    return HttpResponse('<h1> a ete ajouter avec success dans le group premium</h1>')