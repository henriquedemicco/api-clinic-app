from django.db import models
from uuid import uuid4

# Create your models here.
    
class Paciente(models.Model):
    id_paciente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    data_nascimento = models.CharField(verbose_name="Data de Nascimento", max_length=10)
    email = models.CharField(max_length=90)

    def __str__(self):
        return self.nome


