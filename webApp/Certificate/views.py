from django.shortcuts import render
from django.http import HttpResponse
from mainApp.CertificateGenerator import generateCertificate, sendEmail
from .models import participant
# Create your views here.

def info(request):
        # generateCertificate(Pre, id, name)
    context = {

    }
    if request.method == "POST":
        Pre = request.POST.get("Pre")
        Id = request.POST.get("Id")
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        context['Object'] = participant.objects.create(Pre = Pre, id = Id, Name = Name, Email = Email)
        context['Created'] = True
    return render(request, 'main.html', context=context)