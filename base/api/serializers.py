from dataclasses import field
from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSeriaizer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
