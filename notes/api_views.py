from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter

from .serializers import NoteSerializer
from .models import Note


class NoteAPIViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (OrderingFilter,)
    ordering = ['-id']

    def get_queryset(self):
        return self.request.user.notes.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
