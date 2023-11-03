from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('enviar-solicitud-a-chat-gpt/',
         views.solicitud_chat_gpt, name="solicitud_chat_gpt"),

]
