from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required

from App_Login.models import User
import json




def signupView(request):
    return render(request, 'signupView.html', context={'title':'signup'})

def signup_user(request):
    if request.method == 'POST':
        if request.method == 'POST': 
            email = request.POST['email']
            password = request.POST['password']
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user:
                messages.warning(request, "User already exists!!!")
                return JsonResponse({"ret_data":"false"})
            else:
                user_obj = User.objects.create(email=email, password = password, is_active = True)
                data = serializers.serialize('json', [user_obj,])
                struct = json.loads(data)
                data = json.dumps(struct[0])
                return JsonResponse(data, safe=False)
    # return render(request, 'login.html')

def loginView(request):
    next = "/rmail"
    if next in request.GET:
        # print(next)
        next = request.GET['next'] 
    # print("next")
    # print(next)
    return render(request, 'login.html', context={'title':'login','next': next})

def login_user(request):
    if request.method == 'POST':
        if request.method == 'POST': 
            email = request.POST['email']
            password = request.POST['password']
                
            try:
                userCheck = User.objects.get(email=email)
            except User.DoesNotExist:
                userCheck = None
            if userCheck:
                try:
                    user = User.objects.get(email=email, password=password)
                except User.DoesNotExist:
                    user = None
                if user:
                    login(request, user)
                    return JsonResponse({"ret_data":"true"})
                else:
                    return JsonResponse({"ret_data":"false"})
            else:
                return JsonResponse({"ret_data":"email is not exist!!"})
            
            
                

    return render(request, 'login.html')


def page404(request):
    return render(request, 'page404.html')


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    return render(request, 'login.html', context={'title':'login'})
