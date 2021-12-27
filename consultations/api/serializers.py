from rest_framework import serializers
from consultations import models

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = ['id_consulta',
                  'paciente',
                  'info',
                  'data_format',
                ]
