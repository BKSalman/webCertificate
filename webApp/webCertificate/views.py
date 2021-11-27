from django.shortcuts import render
from django.http import HttpResponse
from mainApp.CertificateGenerator import generateCertificate, sendEmail
# Create your views here.

def info(request):
    if request.method == "POST":
        Pre = request.POST.get("Pre")
        id = request.POST.get("ID")
        name = request.POST.get("name")
        generateCertificate(Pre, id, name)
        email = request.POST.get("email")
    context = {}
    return render(request, 'main.html', context=context)