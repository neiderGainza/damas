from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json
from login import models as login_models

# Create your views here.
def home(request):
    if not  request.session['login']:
        return HttpResponseRedirect(reverse("home:login:login"))

    if request.method == "POST":
        infor = json.load(request)
        if infor['accion'] == "cerrar_sesion":
            request.session['login'] = False
            del request.session['name']
            return JsonResponse({})
        elif infor['accion'] == "perfil":
            usuario = login_models.User.objects.filter(name = request.session['name'])[0]

            return JsonResponse( {
                "name":usuario.name,
                "description":usuario.description,
                "elo":usuario.elo,
                "partidas_jugadas":usuario.partidas_jugadas,
            } )


    return render(request, "home/home.html", {"login":True})

