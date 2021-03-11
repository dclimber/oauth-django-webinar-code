from rest_framework import viewsets

from .models import Poet
from .serializers import PoetSerializer


class PoetViewSet(viewsets.ModelViewSet):

    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
