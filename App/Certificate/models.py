from django.db import models
from django.conf import settings
from django.db.models.enums import Choices

# Create your models here.


class participant(models.Model):
    Pre = models.TextField()
    id = models.TextField(primary_key=True)
    Name = models.CharField(max_length=300)
    Email = models.CharField(max_length=300)
    image = models.ImageField('img', upload_to = '', default = 'media/Certificate 5.png')
    def __str__(self):
        return self.id +' '+ self.Name


class Rating(models.Model):
    choices = (
        ('Excellent','Excellent'),
        ('Medium','Medium'),
        ('Poor','Poor'),
    )
    Participant = models.ForeignKey(participant, null=True, on_delete=models.SET_NULL)
    Professional = models.CharField(max_length=255, choices= choices)
    Informative = models.CharField(max_length=255, choices= choices)
    VisuallyPleasing = models.CharField(max_length=255, choices= choices)