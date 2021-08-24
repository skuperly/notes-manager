from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import NoteAPIViewSet


router = DefaultRouter()
router.register('notes', NoteAPIViewSet, basename='notes_api_viewset')


urlpatterns = [
    path('api/', include(router.urls)),
]
