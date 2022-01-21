from rest_framework import viewsets
from core.api import serializers
from core import models

from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()