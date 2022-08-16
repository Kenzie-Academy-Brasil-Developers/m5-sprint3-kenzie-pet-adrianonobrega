from pyexpat import model
from django.db import models

# Create your models here.

from django.db import models







class Sex(models.TextChoices):
    macho = "Macho"
    femea = "Femea"
    default = "Não informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15, choices=Sex.choices,default=Sex.default)
    
    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="animals")
    traits = models.ManyToManyField("traits.Trait")

   



    
    
    