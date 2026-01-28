from rest_framework import serializers
from ..models import Diagram
from .node import DiagramNodeSerializer
from .link import DiagramLinkSerializer

class DiagramSerializer(serializers.ModelSerializer):
    nodes = DiagramNodeSerializer(many=True, read_only=True)
    links = DiagramLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Diagram
        fields = [
            "id",
            "name",
            "description",
            "nodes",
            "links",
            "created_at",
        ]
