from rest_framework.viewsets import ReadOnlyModelViewSet

from news.models import News
from news.serializers import NewsModelSerializer
from news.paginations import NewsPagination


class NewsModelViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    pagination_class = NewsPagination