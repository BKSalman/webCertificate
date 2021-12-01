from django.urls import path
from . import views
from .views import info

urlpatterns = [

    path('', views.info),
    # path('media/',views.info, name='media_path')

]