from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['enterprise_or_government', 'person_reporting', 'incident_details', 'priority']