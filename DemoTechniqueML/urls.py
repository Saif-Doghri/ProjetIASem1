from django.urls import path,include
from .views import *

urlpatterns=[
    path('',homepage),
    path('Predictive/',include('Predictive.urls'))
]