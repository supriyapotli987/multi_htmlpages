"""
URL configuration for project15 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('averages/',avereges,name='averages'),
    path('course/',course,name='course'),
    path('timetable/',timetable,name='timetable'),
    path('seminar/',seminar,name='seminar'),
    path('institute/',institute,name='institute'),
    path('anchortag/',anchortag,name='anchortah'),
    path('background/',background,name='background'),
    path('box/',box,name='box'),
    path('buttons/',buttons,name='buttons'),
    path('calculator/',calculator,name='calculator'),
    path('csspositions/',csspositions,name='csspositions'),
    path('register/',register,name='register'),
    path('semantic/',semantic,name='semanctic'),
    path('semanticvideo/',semanticvideo,name='semanticvideo'),
    path('student/',student,name='student'),
    path('textformating/',textformating,name='textformating'),
    path('translate/',translate,name='translate'),
    path('movie/',movie,name='movie'),
    path('emp/',emp,name='emp'),
    path('rotate/',rotate,name='rotate'),
    path('zomato/',zomato,name='zomato'),
]
