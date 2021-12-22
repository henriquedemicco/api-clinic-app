from rest_framework import serializers
from address import models

class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enderecos
        fields = ['id_endereco',
                  'paciente',
                  'rua',
                  'numero',
                  'bairro',
                  'cidade',
                  'estado',
                ]
