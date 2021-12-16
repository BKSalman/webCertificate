from django.urls import path
from . import views
from .views import info, Certificate

urlpatterns = [

    path('', views.info, name='home_form'),
    path('Certificate/',views.Certificate, name='Certificate')

]