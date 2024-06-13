from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений!!!"""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AdvertisementFilter
    search_fields = ["status", "created_at"]
    ordering_fields = ["user", "created_at"]
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
