from rest_framework.viewsets import ReadOnlyModelViewSet

from documents.models import Document
from documents.serializers import DocumentSerializer


class DocumentViewSet(ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer