from rest_framework import viewsets
from .models import WaitlistEntry
from .serializer import WaitlistEntrySerializer
from .pagination import CustomPagination
from rest_framework import filters


class WaitlistEntryViewSet(viewsets.ModelViewSet):
    queryset = WaitlistEntry.objects.all().order_by('-timestamp')
    serializer_class = WaitlistEntrySerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['email', 'name']
    ordering_fields = ['timestamp']
    
    
    
    
    