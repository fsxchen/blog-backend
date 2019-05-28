from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


from base.utils import CustomeLimitOffsetPagination

from .models import Poem
from .serializers import PoemSerializer


class PoemViewset(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    pagination_class = CustomeLimitOffsetPagination
    # 过滤，搜索，排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = ArticleFilter
    search_fields = ('auth_name',)