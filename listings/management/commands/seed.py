# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_titles = ["Cozy Cottage", "Modern Apartment", "Beach House", "City Loft", "Country Retreat"]
        for i in range(10):
            Listing.objects.create(
                title=random.choice(sample_titles) + f" #{i+1}",
                description="A lovely place to stay!",
                price_per_night=round(random.uniform(50, 300), 2),
                max_guests=random.randint(1, 8)
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded sample listings."))
