from django.urls import path
from App_Login import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'App_Login'


urlpatterns = [
    path('signup', views.signupView, name='signup'),
    path('signup/insert', views.signup_user, name='signUser'),
    path('login', views.loginView, name='login'),
    path('login/insert', views.login_user, name='loginUser'),
    path('logout', views.logout_user, name='logout'),
    path('page404', views.page404, name='page404'),
]