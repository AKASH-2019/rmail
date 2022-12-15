from django.db import models
# from django.contrib.auth.models import User
from App_Login.models import User


# Create your models here.

class EmailCategory(models.Model):
    title = models.TextField(max_length=20, blank=False)
    details = models.TextField(max_length=200)

class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    subject = models.TextField(max_length=50, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    category = models.TextField(blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date', ]