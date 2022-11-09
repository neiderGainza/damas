from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from login import models as login_model
import json


def jugadores(request):
    
    if request.method == "POST":
        datos = json.load(request)
        if datos['accion'] == "rellenarLista":
            arr = [[i.name, i.elo_bala, i.elo_rapido,True] for i in login_model.User.objects.all()[:10]]
            return JsonResponse({"lista_jugadores": arr,})
        
        if datos['accion'] == "search":
            try:
                user = login_model.User.objects.get(name = datos['cadena'])
                return JsonResponse({"error":False, "user": [user.name, user.elo_bala, user.elo_rapido,True]})
            except:
                return JsonResponse({"error":True})
