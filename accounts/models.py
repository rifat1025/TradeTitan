from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("SELLER", "Seller"),
        ("WHOLESALER", "Wholesaler"),
        ("BUYER", "Buyer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="BUYER")

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email