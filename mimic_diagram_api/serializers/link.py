from rest_framework import serializers
from ..models import DiagramLinkEndpoint, DiagramLink

class DiagramLinkEndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagramLinkEndpoint
        fields = "__all__"


class DiagramLinkSerializer(serializers.ModelSerializer):
    endpoints = DiagramLinkEndpointSerializer(many=True, read_only=True)

    class Meta:
        model = DiagramLink
        fields = "__all__"