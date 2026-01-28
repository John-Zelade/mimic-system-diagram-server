# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ._views.auth_views import UserViewSet, GroupViewSet, RegisterView, LoginView, PermissionViewSet, RoleViewSet, RolePermissionViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'role-permissions', RolePermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
