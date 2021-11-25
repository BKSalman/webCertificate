from django.urls import path
from . import views

urpatterns = [

    path('hi/', views.say_hi)

]