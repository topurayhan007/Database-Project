from django.urls import path
from . import views

# URL Configurations
urlpatterns = [
    #path('hello/', views.say_hello),
    # path('chart', views.home, name='chartLayout'),
    path('login', views.loginpage, name='loginpage'),
    path('dashboard', views.dashboardpage, name='dashboardpage'),
    path('logout', views.logout_request, name='logout'),
    path('ClassSizeRequirement', views.ClassSizeRequirementView, name='ClassSizeRequirement'),
    path('ClassSizeDistribution', views.ClassSizeDistributionView, name='ClassSizeDistribution'),
    path('UsageOfTheResources', views.UsageOfTheResourcesView, name='UsageOfTheResources'),

]