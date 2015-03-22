from django.http import HttpResponse
from django.shortcuts import render
from portalapp.models import SampleUser,UserInfo, Department, Degree
from portalapp.forms import getUserInfo
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import re
from django.views.generic.edit import UpdateView
from django.db.models import Q
import json
from django.db import transaction

def index(request):
    if request.method == 'GET':
        user_list = SampleUser.objects.all()
        return render(request, 'portalapp/index.html', {
            'user_list': user_list,
            })
    elif request.method == 'POST':
        user = SampleUser()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        return HttpResponse("db update successful")

def get_data_from_email(roll_no):
    department_code = roll_no[:2].lower()
    year_of_admission = 2000+int(roll_no[2:4])
    start_sno = re.search("\d", roll_no[4:]).start()
    degree_code=  roll_no[4:4+start_sno].lower()
    sno=  int(roll_no[4+start_sno:])
    department = Department.objects.get(code=department_code)
    degree = Degree.objects.get(code=degree_code)
    return {'department':department.id,'degree':degree.id,'roll_no':sno, 'year_of_admission':year_of_admission}


def create_userinfo(request):
    if request.method == 'GET':
        try:
            user = request.user
            data = get_data_from_email(user.username)
            form = getUserInfo(initial=data)
        except:
            form  = getUserInfo()
            pass
        return render(request, 'portalapp/userinfo_form.html', {
            'form': form,
            })
    elif request.method == 'POST':
        form = getUserInfo(request.POST)
        if form.is_valid():
            userinfo = form.save(commit=False)
            user = User.objects.get(username=request.user)
            userinfo.user=user
            userinfo.status=1
            userinfo.save()
        return HttpResponse("db update successful")

class UserInfoUpdate(UpdateView):
    model = UserInfo
    template_name_suffix = '_form'
    form_class = getUserInfo

    def get_success_url(self):
        return reverse("portalapp:view_userinfo")

def view_userinfo(request):
    user = request.user
    userinfo = get_object_or_404(UserInfo,user=user)
    return render(request, 'portalapp/userinfo.html', {
            'userinfo': userinfo,
            })

@transaction.commit_on_success
def search_name(request):
    search_str=request.GET.get('q', '')
    user_data=[]
    #import pdb;pdb.set_trace();
    search_terms= search_str.split()
    if len(search_terms) == 1:
        users = User.objects.filter(Q(first_name__contains=search_terms[0]) | Q(last_name__contains=search_terms[0]) )[:5]
    elif len(search_terms) == 2:
        users = User.objects.filter(Q(first_name__contains=search_terms[0]) | Q(last_name__contains=search_terms[1]) )[:5]
    elif len(search_terms) > 2:
        users = User.objects.filter(Q(first_name__contains=search_terms[0]) | Q(last_name__contains=search_terms[1]) )[:5]
    else:
        users = User.objects.filter(Q(first_name__contains=search_str) | Q(last_name__contains=search_str) )[:5]
    for user in users:
        user_data.append({'first_name':user.first_name, 'last_name':user.last_name, 'user_id':user.username})
    #json_data=  json.dumps(json_data)
    return HttpResponse(json.dumps(user_data), content_type="application/json")

def search(request):
    return render(request, 'portalapp/search.html', {})


