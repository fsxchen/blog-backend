from rest_framework import viewsets

from base.utils import CustomeLimitOffsetPagination

from .models import Poem
from .serializers import PoemSerializer


class PoemViewset(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    pagination_class = CustomeLimitOffsetPagination