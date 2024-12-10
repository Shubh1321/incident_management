from rest_framework import serializers
from .models import Incident
from utils.helpers import validate_incident_priority

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

    def validate_priority(self, value):
        validate_incident_priority(value)
        return value