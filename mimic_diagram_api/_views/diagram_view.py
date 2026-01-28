from rest_framework import viewsets
from ..models import Diagram
from ..serializers.diagram import DiagramSerializer

# Create Diagram
class DiagramViewSet(viewsets.ModelViewSet):
    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer

#Retrieve Diagram along with the link and node in it