from django.urls import path

from . import views

urlpatterns = [
    path('', views.predictionpv,name='predPrixVente'),
    path('result/',views.result),
]
