from django.shortcuts import render
from django.http import HttpResponse
from .CertificateGenerator import generateCertificate, sendEmail
from .models import participant
# Create your views here.

def info(request):
    context = {

    }
    if request.method == "POST":
        Pre = request.POST.get("Pre")
        Id = request.POST.get("Id")
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        context['Object'] = participant.objects.create(Pre = Pre, id = Id, Name = Name, Email = Email)
        context['Created'] = True
        generateCertificate(Pre= Pre, Id= Id, Name= Name)
        context['img'] = generateCertificate.image
        print(generateCertificate.image.image.url)
        return render(request, 'Certificate.html', context=context)
    else:
        return render(request, 'main.html')
        