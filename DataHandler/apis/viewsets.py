from rest_framework import viewsets
from .serializers import ResponseSerializer
from .models import Response

class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()