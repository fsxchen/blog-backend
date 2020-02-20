from rest_framework import status, viewsets, filters, mixins
from .models import DailyThink
from .serializers import DailyThinkSerializer
from base.utils import CustomeLimitOffsetPagination


class DailyThinkViewset(viewsets.ModelViewSet):
    queryset = DailyThink.objects.all()
    serializer_class = DailyThinkSerializer

    pagination_class = CustomeLimitOffsetPagination