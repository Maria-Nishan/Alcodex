from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('check',views.check,name='check'),
    path('index/',views.index,name='index'),   
    path('main/',views.main,name='main'),
    path('register/',views.register,name='register'),
    path('fillform/',views.fill,name='fillform'),
    path('adgroup/',views.adgroup,name='adgroup'),
    path('saveadgroup/',views.saveAdgroup,name='saveadgroup'),
    path('adlocation/',views.adlocation,name='adlocation'),
    path('adstudent/',views.adstudent,name='adstudent'),
    path('savestudent/',views.savestudent,name='savestudent'),




   
    


    
]