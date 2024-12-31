from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        
        # 2 méthodes pour exclure un champ du serializer
        fields = ['id', 'nom', 'code_postal', 'adresse']  # numero_siret exclu
        # exclude = ['numero_siret'] # numero_siret exclu

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'
