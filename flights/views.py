from rest_framework.generics import ListAPIView
from .models import Booking, Flight
from flights.serializers import FlightListSerializer, BookingListSerializer
from django.utils import timezone

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

    def get_queryset(self):
        return super().get_queryset().filter(date__gt=timezone.now())
