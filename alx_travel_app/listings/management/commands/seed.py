from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **kwargs):
        # Sample data to insert
        sample_listings = [
            {
                "property_name": "Cozy Beach Cabin",
                "location": "Mombasa",
                "price_per_night": 120.00,
                "description": "A beautiful cabin right by the ocean."
            },
            {
                "property_name": "Urban Studio",
                "location": "Nairobi",
                "price_per_night": 85.00,
                "description": "Modern studio in the heart of the city."
            },
            {
                "property_name": "Mountain Retreat",
                "location": "Nanyuki",
                "price_per_night": 200.00,
                "description": "Escape to the fresh air of the mountains."
            }
        ]

        for data in sample_listings:
            Listing.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {data["property_name"]}'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))