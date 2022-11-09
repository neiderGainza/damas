from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from .urls import*
from . import models
# Create your views here.




def login(request):
    if request.method == "POST":
        if not models.User.objects.filter(name = request.POST['userName']): 
            return render(request, "login/login.html", {"error":"Nombre de usuario no existe"})
        else:
            if request.POST["Password"] != models.User.objects.get(name \
                = request.POST["userName"]).password:
                return render(request, "login/login.html", {"error":"Usuario o contraseña incorrectos"})
        
        request.session["login"] = True
        request.session["name"] = request.POST["userName"]
        return HttpResponseRedirect(reverse("home:home"))

    return render(request, "login/login.html", {})



def new(request):
    
    if request.method == "POST":
        if models.User.objects.filter(name = request.POST['userName']): 
            return render(request, "login/new.html", {"error":"Nombre de usuario en uso"})
        
        if request.POST["Password"] != request.POST["Password2"]:
            return render(request, "login/new.html",\
                 {"error":"Las contraseñas no son iguales"})

        if len(request.POST["Password"]) < 8:
            return render(request, "login/new.html",\
                 {"error":"La contraseña es muy corta"})

        #a falta de validacion
        nuevo_usuario = models.User(name= request.POST['userName'],email = request.POST['Email'],password = request.POST['Password'])
        nuevo_usuario.save()
            
        return HttpResponseRedirect(reverse("home:login:login"))

    return render(request, "login/new.html", {})





