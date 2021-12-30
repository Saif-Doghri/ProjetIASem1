from django.shortcuts import render
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Create your views here.
from django.http import HttpResponse


def predictionpv(request):
    return render(request, "predictionpv.html")

def result(request):
    with open("PredictionPrixVente/prediction.sav","rb") as f:
        model=pickle.load(f)
    v=float(request.GET['pa'])
    prix=model.predict([[v]])
    return render(request, "predictionpv.html",{"result2":prix})
