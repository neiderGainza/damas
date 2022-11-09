from django.urls import path,include
from . import views


app_name = "login"
urlpatterns = [
    path('', views.login, name='login'),
    path('new/', views.new, name='new'),
]