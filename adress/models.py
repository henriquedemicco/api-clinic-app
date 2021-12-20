from django.db import models
from core.models import Pacientes
from uuid import uuid4

# Create your models here.

class Enderecos(models.Model):
    id_endereco = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    rua = models.CharField(max_length=150)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)