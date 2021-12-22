from django.db import models
from core.models import Paciente
from uuid import uuid4
from django.db.models import *
from datetime import *

# Create your models here.

class Consultation(models.Model):
    id_consulta = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    info = models.TextField(verbose_name="Informações sobre a consulta")
    data = models.DateTimeField(verbose_name="Data e Horário")

    
    def __str__(self):
        return self.data
    
    def data_format(self):
        return self.data.strftime('%d/%m/%Y')