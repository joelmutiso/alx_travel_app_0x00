from rest_framework import serializers
from django.db import models
from ..models import Listing, Booking, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    """Minimal serializer for related User data (Host/Guest/Reviewer)."""
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'email', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model."""
    reviewer = UserDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'reviewer', 'created_at']
        read_only_fields = ('reviewer', 'listing')

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""
    guest = UserDetailSerializer(read_only=True)
    listing_title = serializers.CharField(source='listing.title', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'check_in_date', 
            'check_out_date', 'total_price', 'status', 'created_at'
        ]
        read_only_fields = ('guest', 'total_price', 'status', 'created_at')

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model, including nested Reviews and Bookings."""
    host = UserDetailSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    # Calculate average rating
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night', 'host', 
            'city', 'country', 'max_guests', 'reviews', 'average_rating',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('reviews', 'average_rating', 'host', 'created_at', 'updated_at')
    
    def get_average_rating(self, obj):
        """Calculates the average rating from all associated reviews."""
        if obj.reviews.exists():
            # Use floating point calculation for average
            return obj.reviews.aggregate(models.Avg('rating'))['rating__avg']
        return 0.0