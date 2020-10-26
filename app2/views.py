from django.shortcuts import render,redirect, get_object_or_404
from app2.models import UserModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):

    return render(request,'index.html')


def save_user(request):
    un = request.POST.get("un")
    ue = request.POST.get("ue")
    up = request.POST.get("up")
    ut = request.POST.get("type")
    UserModel(uemail=ue,uname=un,upass=up,admin=ut).save()
    return redirect(request,'user_registration.html')


def user_register(request):
    return render(request,"user_registration.html")

def login_check(request):
    un= request.POST.get("un")
    up= request.POST.get("up")
    rec = UserModel.objects.get(uemail=un)
    if rec:
        if rec.upass == up:
            if rec.admin == 'True':
                return redirect('admin_home')
            else:
                return redirect('user_home')
        else:
            messages.error(request,"Invalid Password")
    else:
        messages.error(request,"Invalid User")

@login_required(login_url='index.html')
def admin_home(request, id = None):
    res = UserModel.objects.all()
    context={}
    context['user']=get_object_or_404(UserModel,id=id)
    return render(request,'admin.html',{"data":res})


def user_home(request):
    res = UserModel.objects.all()
    return render(request,'user.html',{"data":res})
