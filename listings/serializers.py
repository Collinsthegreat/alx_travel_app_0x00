from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "description",
            "price_per_night",
            "max_guests",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "listing",
            "user",
            "start_date",
            "end_date",
            "status",
            "created_at",
        ]
        read_only_fields = ("created_at",)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "listing",
            "user",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = ("created_at",)
