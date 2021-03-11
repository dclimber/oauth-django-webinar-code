from rest_framework import serializers

from .models import Poem, Poet


class PoetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poet
        fields = ('first_name', 'last_name', 'bio', 'photo_url')


class PoemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poem
        fields = ['author', 'title', 'text', 'year']
