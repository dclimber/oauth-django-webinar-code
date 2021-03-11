from rest_framework import viewsets

from .models import Poem, Poet
from .serializers import PoemSerializer, PoetSerializer


class PoetViewSet(viewsets.ModelViewSet):

    queryset = Poet.objects.all()
    serializer_class = PoetSerializer


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
