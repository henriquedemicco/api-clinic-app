from rest_framework import serializers
from core import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ad
        fields = ['id_paciente',
                  'nome',
                  'sexo',
                  'enderecos',
                  'cpf',
                  'celular',
                  'data_nascimento',
                  'email',
                ]
