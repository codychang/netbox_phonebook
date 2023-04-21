from netbox.api.viewsets import NetBoxModelViewSet
from .. import filtersets, models
from .serializers import NumberSerializer

class NumberViewSet(NetBoxModelViewSet):
    queryset = models.Number.objects.all()
    serializer_class = NumberSerializer
    filterset_class = filtersets.NumberFilterSet