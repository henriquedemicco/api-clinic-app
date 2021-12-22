from rest_framework import serializers
from core import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = ['id_paciente',
                  'nome',
                  'sexo',
                  'cpf',
                  'celular',
                  'data_nascimento',
                  'email',
                ]
