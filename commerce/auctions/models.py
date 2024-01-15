from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"
    
    
class Bid(models.Model):
    amount = models.FloatField() 
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return  f"User {self.bidder.username} bid {self.amount}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(null=True, max_length=300)
    imageUrl = models.CharField(null=True, blank=True, max_length=1000)
    initialp = models.FloatField(null=True, blank=True)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank="True", null="True", related_name="bid")
    active = models.BooleanField(default=True)
    owner =models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True, related_name="similar_listings")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="usersWatching")
 
    def __str__(self):
        return f"{self.title}: {self.price}$"

class Comments(models.Model):
    message = models.TextField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now) 
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE, related_name="user_comment")
    listing = models.ForeignKey(Listing, null = True, blank = True, on_delete=models.CASCADE, related_name="listing_comment")
  
    def get_date(self):
        return self.date_created.strftime('%B %d %Y')

class Picture(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="pictures")
    picture = models.ImageField(upload_to="images/")
    text = models.CharField(max_length=140) 