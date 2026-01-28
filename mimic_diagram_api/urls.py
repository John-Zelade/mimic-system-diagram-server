from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ._views.diagram_view import DiagramViewSet
from ._views.node_view import NodeView
from ._views.link_view import LinkView

router = DefaultRouter()
router.register(r'diagrams', DiagramViewSet)

urlpatterns =[
    path('',include(router.urls)),

    # Custom Node creation endpoint
    path('nodes/', NodeView.as_view(), name='node-create'),
    
    # Custom Link creation endpoint
    path('links/', LinkView.as_view(), name='link-create'),
] 

