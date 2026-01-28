from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import DiagramLink, DiagramLinkEndpoint
from ..serializers.link import DiagramLinkSerializer, DiagramLinkEndpointSerializer

class LinkView(APIView):
    def post(self, request):
        endpoints_data = request.data.pop("endpoints", [])

        link_serializer = DiagramLinkSerializer(data=request.data)
        if link_serializer.is_valid():
            link = link_serializer.save()

            # create endpoints using _id
            for ep_data in endpoints_data:
                DiagramLinkEndpoint.objects.create(
                    link=link,
                    role=ep_data.get("role", "from"),
                    node_id=ep_data["node"],
                    port_id=ep_data.get("port")
                )

            link.refresh_from_db()
            return Response(DiagramLinkSerializer(link).data, status=status.HTTP_201_CREATED)
        else:
            return Response(link_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
