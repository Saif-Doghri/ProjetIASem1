from django.urls import path,include

urlpatterns=[
    path('PredictStock/',include('PredictionStock.urls'))
]