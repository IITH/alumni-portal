from django.http import HttpResponse
from django.shortcuts import render
from portalapp.models import UserInfo


# Create your views here.

def index(request):
    if request.method == 'GET':
        user_list = UserInfo.objects.all()
        return render(request, 'portalapp/index.html', {
            'user_list': user_list,
            })
    elif request.method == 'POST':
        user = UserInfo()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        return HttpResponse("db update successful")
