from rest_framework import viewsets
from adress.api import serializers
from adress import models

class EnderecosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Enderecos.objects.all()