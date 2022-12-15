from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

import json
import os
import App_Email.categoryCheck as cat

from App_Email.models import Email, EmailCategory
from App_Login.models import User


@login_required
def homeView(request):
    primary = Email.objects.filter(receiver=request.user, category='primary')
    social = Email.objects.filter(receiver=request.user, category='social')
    promotions = Email.objects.filter(receiver=request.user, category='promotions')
    forum = Email.objects.filter(receiver=request.user, category='forum')
    return render(request, 'homeView.html', context={'title':'home','forum': forum, 'promotions': promotions,
                            'social':social, 'primary':primary})

@login_required
def emailCreateView(request):
    return render(request, 'emailCreateView.html', context={'title':'create'})

@login_required
def emailInsert(request):
    if request.method == 'POST': 
        receipents = request.POST['email']
        sub = request.POST['sub']
        message = request.POST['message']
        
        # email category check algorithm +++++++++++++++++++++++++++++++++++++++++++++++++++++
        category_email = cat.category_check(sub,message,receipents)

        # print(category_email)
        try:
            receipents = User.objects.get(email=receipents)
        except User.DoesNotExist:
            receipents = None
        if receipents and receipents != request.user:
            email_obj = Email.objects.create(message=message, subject = sub, sender=request.user, receiver=receipents, category=category_email)
            data = serializers.serialize('json', [email_obj,])
            struct = json.loads(data)
            data = json.dumps(struct[0])
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"ret_data":"false"})
            

@login_required
def emailDetail(request,py):
    print(py)
    try:
        email = Email.objects.get(pk=py)
    except Email.DoesNotExist:
        email = None
    if email:
        rcvUsername = str(email.receiver)
        sendUsername = str(email.sender)
        word1 = rcvUsername.split('@')
        word2 = sendUsername.split('@')
        return render(request, 'emailDetail.html', context={'title':email.subject, 'email': email, 'rcvUsername': word1[0], 'sendUsername': word2[0]})
    else:
        return render(request, 'page404.html')

@login_required
def emailSent(request):
    email = Email.objects.filter(sender=request.user)
    return render(request, 'emailList.html', context={'email': email, 'email_type': 'sent', 'title': 'sent'})


@login_required
def emailListByCategory(request,slug):
    print(slug)
    try:
        emailCategory = EmailCategory.objects.filter(title=slug)
    except EmailCategory.DoesNotExist:
        emailCategory = None
    if emailCategory:
        email = Email.objects.filter(receiver=request.user, category=slug)
        return render(request, 'emailList.html', context={'email': email, 'email_type': slug, 'title': slug})
    else:
        return render(request, 'page404.html')
        
    
