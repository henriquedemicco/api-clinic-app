from rest_framework import serializers
from adress import models

class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ad
        fields = ['id_endereco',
                  'paciente',
                  'rua',
                  'numero',
                  'bairro',
                  'cidade',
                  'estado',
                ]
