from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('process-login',views.process_login,name='process-login'),
    path('send-message/',views.send_message,name='send-message'), 
    path('rooms/<str:RoomId>',views.room,name='room'),
    path('get/<str:RoomId>',views.get_messages,name='get-messages')

]