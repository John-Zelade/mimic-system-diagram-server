from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import  DiagramNodePort
from ..serializers.node import DiagramNodeSerializer


#Create Node
class NodeView(APIView):
    def post(self, request):
        ports_data = request.data.pop("ports", [])
        
        # create node
        node_serializer = DiagramNodeSerializer(data=request.data)
        if node_serializer.is_valid():
            node = node_serializer.save()
            
            # create ports
            for port_data in ports_data:
                DiagramNodePort.objects.create(node=node, **port_data)
            
            # return node with ports
            node.refresh_from_db()
            return Response(DiagramNodeSerializer(node).data, status=status.HTTP_201_CREATED)
        else:
            return Response(node_serializer.errors, status=status.HTTP_400_BAD_REQUEST)