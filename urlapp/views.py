from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import URL
from .serializers import URLSerializer


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
