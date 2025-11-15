from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

# Get the active User model
User = get_user_model()

class Listing(models.Model):
    """
    Represents a property available for booking.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Foreign Key: Link to the User who owns the listing (the 'host')
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # If host is deleted, set their listings' host field to NULL
        null=True,
        related_name='listings'
    )
    
    # Fields for location/details
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    max_guests = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} in {self.city}"

class Booking(models.Model):
    """
    Represents a customer's confirmed or requested booking for a Listing.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    # Foreign Key: Link to the Listing being booked
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE, # If listing is deleted, all associated bookings are deleted
        related_name='bookings'
    )
    
    # Foreign Key: Link to the User making the booking
    guest = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # If guest is deleted, all their bookings are deleted
        related_name='guest_bookings'
    )
    
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for {self.listing.title} by {self.guest.email}"

class Review(models.Model):
    """
    Represents a review left by a user on a specific Listing.
    """
    # Foreign Key: Link to the Listing being reviewed
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE, # If listing is deleted, all reviews are deleted
        related_name='reviews'
    )
    
    # Foreign Key: Link to the User who wrote the review
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # If reviewer is deleted, their reviews are deleted
        related_name='reviews_written'
    )
    
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} star review for {self.listing.title}"