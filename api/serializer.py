from rest_framework import serializers

from cakes.models import Cake


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = "__all__"
