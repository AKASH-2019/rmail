from django.urls import path
from App_Email import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'App_Email'


urlpatterns = [
    path('', views.homeView, name='home'),
    path('create', views.emailCreateView, name='emailCreate'),
    path('insert', views.emailInsert, name='emailInsert'),
    path('details/<py>', views.emailDetail, name='emailDetail'),
    path('sent', views.emailSent, name='emailSent'),
    path('category/<slug>', views.emailListByCategory, name='emailDetail'),

]