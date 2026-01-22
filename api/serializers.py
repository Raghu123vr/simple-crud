from rest_framework import serializers
from .models import Restapi

class Restserializer(serializers.ModelSerializer):
    class Meta:
        model = Restapi
        fields = "__all__"