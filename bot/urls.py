from django.urls import path
from . import views

app_name = 'bot'

urlpatterns = [
    path('', views.bot_page, name='bot')
    ]