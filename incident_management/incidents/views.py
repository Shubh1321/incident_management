from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .models import Incident
from .serializers import IncidentSerializer
from utils.helpers import generate_incident_id  # Assuming this function is in your helpers.py

class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(reporter=self.request.user)

    def perform_create(self, serializer):
        incident_id = generate_incident_id()  # Assuming generate_incident_id generates a unique ID
        serializer.save(reporter=self.request.user, incident_id=incident_id)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.status == 'Closed':
            raise ValidationError("This incident is closed.")
        else:
            serializer.save()