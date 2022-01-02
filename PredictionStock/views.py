import os.path

from django.shortcuts import render
import joblib
from statsmodels.tsa.arima_model import ARIMAResults
import pickle
import statsmodels
import pandas as pd
import plotly.express as px
import plotly.offline as opf
import pyodbc as driver

from .apps import *


# Create your views here.
def stockpredictionhome(request):
    connect = driver.connect('Driver={SQL Server};'
                             'Server=DESKTOP-E14KD8F;'
                             'Database=DWPharma;'
                             'Trusted_Connection=yes;')
    connect1 = driver.connect('Driver={SQL Server};'
                              'Server=DESKTOP-E14KD8F;'
                              'Database=pharm_SA;'
                              'Trusted_Connection=yes;'
                              )
    if request.method == 'GET':
        return render(request, 'PredictionStock/PredictStock.html')
    elif request.method == 'POST':
        df_stock = pd.read_sql_query("Select * from FaitStock", connect)
        df_stock = df_stock.drop(columns=["Article_Fk"])
        df_stock = df_stock.loc[df_stock["TypeMouvement"] == "Entrée"]
        df_stock['Date_Fk'] = df_stock["Date_Fk"].apply(pd.to_datetime)
        df_stock = df_stock.groupby(['Date_Fk']).mean()
        df_stock.index = pd.DatetimeIndex(df_stock.index).to_period('D')
        model = pd.read_pickle('PredictionStock/Models/mymodel.pkl')
        value = model.predict(start=request.POST['startdate'], end=request.POST['enddate'])
        fig = px.bar(df_stock, x=df_stock.index.to_timestamp(), y="Qte", labels=dict(x="Date", Qte="Quantite"))
        fig_div = opf.plot(fig, output_type='div')
        return render(request, 'PredictionStock/PredictStock.html', context={'data': fig_div})
