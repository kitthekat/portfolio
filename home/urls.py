from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.main_call, name='home')
    ]
