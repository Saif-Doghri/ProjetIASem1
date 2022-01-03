import os.path

import plotly.tools
from django.shortcuts import render
import joblib
from statsmodels.tsa.arima_model import ARIMAResults
import pickle
import statsmodels
import pandas as pd
import plotly.express as px
import plotly.offline as opf
import pyodbc as driver
import matplotlib.pyplot as plt
from .apps import *


# Create your views here.
def stockpredictionhome(request):
    if request.method == 'GET':
        return render(request, 'PredictionStock/PredictStock.html')
    elif request.method == 'POST':
        sarimax_model = pd.read_pickle('PredictionStock/Models/sarimax_new.pkl')
        arima_model=pd.read_pickle('PredictionStock/Models/arima_model.pkl')
        fig_predic ,ax=plt.subplots()
        if request.POST['model']=='sarimax':
            value = sarimax_model.predict(start=request.POST['startdate'],end=request.POST['enddate'],freq='W')
            value.plot(legend=True)
        if request.POST['model']=='arima':
            value2 = arima_model.predict(start=request.POST['startdate'],end=request.POST['enddate'])
            value2.plot(legend=True)
        fig_predic=plotly.tools.mpl_to_plotly(fig_predic)
        fig_predic_div = opf.plot(fig_predic, output_type='div')
        return render(request, 'PredictionStock/PredictStock.html', context={'predic': fig_predic_div})
