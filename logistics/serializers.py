from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistics.models import SupplyChainParticipant


class SuppliersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyChainParticipant
        exclude = ['debt']
        read_only_fields = ['is_factory']

    def update(self, instance, validated_data):
        if 'debt' in self.initial_data:
            raise ValidationError({'debt': 'Это поле можно изменить только через админку.'})
        return super(SuppliersUpdateSerializer, self).update(instance, validated_data)


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyChainParticipant
        fields = '__all__'
        read_only_fields = ['is_factory']
