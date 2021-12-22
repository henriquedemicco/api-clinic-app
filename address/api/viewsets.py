from rest_framework import viewsets
from address.api import serializers
from address import models

class EnderecosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnderecosSerializer
    queryset = models.Enderecos.objects.all()