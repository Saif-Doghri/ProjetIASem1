from django.shortcuts import render
from .templates import *
import joblib
import pandas as pd
import pyodbc as driver

# Create your views here.
def predCategorie(request):
    my_file = open("Predictive/Models/sample.txt", "r")
    content_list = my_file.read().splitlines()
    #print(content_list)
    li=["Preparation","Parapharmacie","Medicament","Accessoire","Autre","Lait","Produits Chimiques","Homeopathie"]
    if 'subb' in request.POST:
        cls = joblib.load('Predictive/Models/finalized_model.sav')
        sca = joblib.load('Predictive/Models/scaler.sav')
        trans = joblib.load('Predictive/Models/lab_transform.sav')
        # ans = cls.predict([lis])
        wee = trans.transform([request.POST['codeLabo']])
        serr = pd.Series([request.POST['codeCateg'],
                          request.POST['prixAchat'],
                          request.POST['prixVente'],
                          wee, ]
                         )

        serr = sca.transform([serr])
        ans = cls.predict(serr)

        return render(request, "predcateg.html", context={'ans': li[int(ans)], 'data': content_list})
    # for x in dataD['NomLabo'].unique():
    #    print(x)
    return render(request, "predcateg.html", context={'data': content_list})

    #return render(request, 'predcateg.html')
