from django.urls import path
from . import views
from .views import info

urlpatterns = [

    path('hi/', views.info),

]