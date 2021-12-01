from PIL.Image import Image
from django.shortcuts import render
from django.http import HttpResponse
from .CertificateGenerator import generateCertificate, sendEmail
from .models import participant
from django.conf import settings
from django.core.files import File
# Create your views here.

Participant = participant()

def info(request):

    context = {
        "MEDIA_URL":settings.MEDIA_URL
    }
    if request.method == "POST":
        Pre = request.POST.get("Pre")
        Id = request.POST.get("Id")
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        generateCertificate(Pre= Pre, Id= Id, Name= Name)
        context['Object'] = participant.objects.create(Pre = Pre, id = Id, Name = Name, Email = Email, image= generateCertificate.enc)
        return render(request, 'Certificate.html', context=context)
    else:
        return render(request, 'main.html')
        