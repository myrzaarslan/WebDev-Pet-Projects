from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    current_bid = models.FloatField(blank=True, null=True)
    imgURL = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="listings")
    current_bidder = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="bid")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="listings")

    def __str__(self):
        return self.title

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.FloatField()

    def __str__(self):
        return f"{self.amount} on {self.listing.title} by {self.bidder.username}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.title}"
