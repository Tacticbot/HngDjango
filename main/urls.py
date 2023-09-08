from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musa', views.musa, name='musa'),
    path('api', views.api, name='api')
]

