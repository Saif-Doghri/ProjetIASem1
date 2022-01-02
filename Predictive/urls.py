from django.urls import path,include
from .views import *

urlpatterns=[
    path('',predCategorie,name='predCategorie'),
    path('PredictStock/',include('PredictionStock.urls')),
]
