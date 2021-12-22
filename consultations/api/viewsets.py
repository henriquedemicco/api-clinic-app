from rest_framework import viewsets
from consultations.api import serializers
from consultations import models

class ConsultasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConsultasSerializer
    queryset = models.Consultation.objects.all()