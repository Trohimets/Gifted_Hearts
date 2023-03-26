from rest_framework.serializers import ModelSerializer

from news.models import News, NewsImage

__all__ = (
    'NewsModelSerializer',
    'NewsImageModelSerializer'
)


class NewsImageModelSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['image', 'news']


class NewsModelSerializer(ModelSerializer):
    news_images = NewsImageModelSerializer(
        many=True
    )

    class Meta:
        model = News
        fields = ['id', 'date', 'title', 'news_full_text', 'news_images',
                  'news_video_link']
