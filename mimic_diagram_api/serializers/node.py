from rest_framework import serializers
from ..models import DiagramNode, DiagramNodePort

class DiagramNodePortSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiagramNodePort
        fields="__all__"

class DiagramNodeSerializer(serializers.ModelSerializer):
    ports = DiagramNodePortSerializer(many=True, read_only=True)

    class Meta:
        model = DiagramNode
        fields = "__all__"
