from django.db import models
from uuid import uuid4
from datetime import *
from adress.models import Enderecos

from django.conf import settings

# Create your models here.
    
class Paciente(models.Model):
    id_paciente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=20)
    enderecos = models.ForeignKey(Enderecos, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=100)
    celular = models.ImageField(upload_to="media", null=True, blank=True, max_length=300)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

