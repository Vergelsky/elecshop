from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from logistics.models import SupplyChainParticipant
from logistics.serializers import SuppliersSerializer, SuppliersUpdateSerializer


class SuppliersViewSet(viewsets.ModelViewSet):
    model = SupplyChainParticipant
    queryset = SupplyChainParticipant.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update'):
            return SuppliersUpdateSerializer
        return SuppliersSerializer
