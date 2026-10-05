from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('update/',update,name="update"),
    path('delete/',delete,name="delete"),
    path('display/',display,name="display"),
    path('employee/',emp,name="employee"),
    path('logout/',logout,name="logout"),
]