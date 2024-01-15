from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

from django.contrib.auth.decorators import login_required

def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isListingWatched = request.user in listingData.watchlist.all()
    comments= Comments.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html",{ 
        "listing":listingData,
        "isListingWatched":isListingWatched,
        "comments": comments,
        "isOwner": isOwner
    })

def close(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.active = False
    listingData.save()
    isOwner = request.user.username == listingData.owner.username
    isListingWatched = request.user in listingData.watchlist.all()
    comments=Comments.objects.filter(listing=listingData)
    return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Your Auction is Closed!",
            "update": True,
            "isOwner": isOwner,
            "isListingWatched": isListingWatched,
            "comments": comments
        })
    
    

def addBid(request, id):
    bid=request.POST['newBid']
    listingData = Listing.objects.get(pk=id)
    isListingWatched = request.user in listingData.watchlist.all()
    comments=Comments.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    if int(bid) > listingData.price.amount:
        updateBid = Bid(bidder=request.user, amount=int(bid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Successfull Bid",
            "update": True,
            "isListingWatched": isListingWatched,
            "comments": comments,
            "isOwner": isOwner

        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Unsuccessfull Bid",
            "update": False,
            "isListingWatched": isListingWatched,
            "comments": comments,
            "isOwner": isOwner
        })

def watchlist(request):
    currentUser = request.user
    listings = currentUser.usersWatching.all()
    return render(request, "auctions/watchlist.html",{
        "listings": listings
                  })

def remove(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def add(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))
  
def index(request):
    activeListings = Listing.objects.filter(active=True)
    allCategories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategories
    })

def display_category(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName = categoryFromForm)
        activeListings = Listing.objects.filter(active=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": activeListings,
            "categories": allCategories
        }) 

          


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def categories(request):
    return render(request, "auctions/categories.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        price = request.POST["price"]
        category = request.POST["category"]
        user = request.user

        categoryData = Category.objects.get(category=category)

        newBid=Bid(amount=float(price), bidder=user)
        newBid.save()

        item = Listing(title=title, description=description, imageUrl=imageurl, initialp=price, price=newBid, category=categoryData, owner=user)
        item.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        allCategories = Category.objects.all() 
        return render(request, "auctions/create.html", {
           "categories": allCategories 
        })
    
def new_comment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['addComment']

    newComment = Comments(
        user=currentUser,
        listing=listingData,
        message=message
    )
    newComment.save() 
    return HttpResponseRedirect(reverse("listing", args=(id, )))




