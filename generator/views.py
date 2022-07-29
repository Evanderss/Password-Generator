from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "generator/home.html")

def about(request):
    # return HttpResponse("Hello world")
    return render(request, "generator/about.html")

def password(request):
    character = list("abcdefghijklmnñopqrstuvwxyz")
    generated_password = ""

    length = int(request.GET.get("length"))
    
    if request.GET.get("uppercase"):
        character.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        character.extend(list("!#$%&/()=?¿"))
    if request.GET.get("numbers"):
        character.extend(list("1234567890"))   
         
    for i in range(length):
        generated_password += random.choice(character)
    
    return render(request, "generator/password.html", {"password": generated_password})