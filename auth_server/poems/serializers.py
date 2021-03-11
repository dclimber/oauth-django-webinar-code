from rest_framework import serializers

from .models import Poet


class PoetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poet
        fields = ('first_name', 'last_name', 'bio', 'photo_url')
