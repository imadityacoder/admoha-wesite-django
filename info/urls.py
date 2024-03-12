from info import views
from django.urls import path

urlpatterns = [
    path('', views.info_home, name='info_home')
]
