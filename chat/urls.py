from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('process-login',views.process_login,name='process-login')
]