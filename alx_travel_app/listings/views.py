from rest_framework import viewsets
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing travel listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for managing property bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for handling user reviews and ratings."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer