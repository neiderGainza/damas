from django.shortcuts import render,reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views import generic
from login import models as login_model
import json


def esta(obj:login_model.User, usuario_actual:login_model.User)->bool:
    if obj in usuario_actual.followers.all():
        return True
    return False

def jugadores(request):

    usuario_actual = ""
    try:
        usuario_actual = login_model.User.objects.get(name = request.session['name'])
    except(BaseException):
        return HttpResponseRedirect(reverse("home:login:login"))

    


    if request.method == "POST":
        datos = json.load(request)
        if datos['accion'] == "rellenarLista":
            arr = [[i.name,i.elo, esta(i,usuario_actual)] for i in login_model.User.objects.all()[:10]]
            return JsonResponse({"lista_jugadores": arr,})
        
        if datos['accion'] == "search":
            try:
                user = login_model.User.objects.get(name = datos['cadena'])
                return JsonResponse({"error":False, "user": [user.name, user.elo,True]})
            except:
                return JsonResponse({"error":True})
        
        if datos['accion'] == "change_seguir":
            try:
                usuario = login_model.User.objects.filter( name = datos['user'])[0]
                if esta(usuario,usuario_actual):
                    obj_relacion = login_model.User.followers.through.objects.filter( from_user_id = usuario_actual.name ).filter( to_user_id = usuario.name)[0]
                    obj_relacion.delete()
                else:
                    login_model.User.followers.through(from_user_id = usuario_actual.name, to_user_id = usuario.name).save()
            except:
                 return JsonResponse({"error":"Exception"})
            
            return JsonResponse({"error":False})
