from django.urls import path
from . import views
from .views import info

urlpatterns = [

    path('', views.info, name='home_form'),
    # path('/',views.info, name='media_path')

]