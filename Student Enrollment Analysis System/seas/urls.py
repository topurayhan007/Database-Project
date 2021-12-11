from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    #path('hello/', views.say_hello),
    path('login', views.loginpage, name='loginpage'),
    path('dashboard', views.dashboardpage, name='dashboardpage'),
]