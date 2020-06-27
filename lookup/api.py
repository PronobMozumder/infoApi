from lookup.models import myinfo
from rest_framework import viewsets, permissions
from. serializer import myinfoSerializer

class myinfoViewSet(viewsets.ModelViewSet):
    queryset = myinfo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = myinfoSerializer