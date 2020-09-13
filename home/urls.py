from django.urls import path
from home import views

urlpatterns = [
    path('', views.main_call, name='home')
    ]
