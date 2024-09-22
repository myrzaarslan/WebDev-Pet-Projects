from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    categories = Category.objects.all()
    if request.method == "POST":
        category = get_object_or_404(Category, name=request.POST["category"])
        listings = Listing.objects.filter(active=True, category=category)
        return render(request, "auctions/index.html", {"listings": listings, "categories": categories})
    elif request.method == "GET":
        listings = Listing.objects.filter(active=True)
        return render(request, "auctions/index.html", {"listings": listings, "categories": categories})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {"message": "Invalid username and/or password."})
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {"message": "Passwords must match."})
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {"message": "Username already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/create.html", {"categories": categories})
    elif request.method == "POST":
        category = get_object_or_404(Category, name=request.POST["category"])
        listing = Listing(
            creator=request.user,
            title=request.POST["title"],
            description=request.POST["description"],
            current_bid=float(request.POST["starting_price"]),
            category=category,
            imgURL=request.POST["image"]
        )
        listing.save()
        return HttpResponseRedirect(reverse("index"))

def listing(request, id):
    listingData = get_object_or_404(Listing, pk=id)
    bidder = bool(listingData.current_bidder)
    isListingInWatchlist = request.user in listingData.watchlist.all() if request.user.is_authenticated else False
    return render(request, "auctions/listing.html", {"listing": listingData, "inWatchlist": isListingInWatchlist, "bidder": bidder, "message": "Congratulations, You closed listing!"})

@login_required
def add_wl(request, id):
    listingData = get_object_or_404(Listing, pk=id)
    request.user.watchlist.add(listingData)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

@login_required
def rem_wl(request, id):
    listingData = get_object_or_404(Listing, pk=id)
    request.user.watchlist.remove(listingData)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

@login_required
def watchlist(request):
    wl_listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {"wl_listings": wl_listings})

@login_required
def bid(request, id):
    listing = get_object_or_404(Listing, pk=id)
    bid_amount = float(request.POST["bid_amount"])
    if bid_amount > listing.current_bid:
        new_bid = Bid(listing=listing, bidder=request.user, amount=bid_amount)
        new_bid.save()
        listing.current_bid = bid_amount
        listing.current_bidder = new_bid.bidder
        listing.save()
        return HttpResponseRedirect(reverse("listing", args=(id,)))
    else:
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "inWatchlist": request.user in listing.watchlist.all(),
            "message": "Bid must be higher than the current bid."
        })

@login_required
def close_auction(request, id):
    listing = get_object_or_404(Listing, pk=id)
    if request.user == listing.creator:
        listing.active = False
        listing.save()
        return HttpResponseRedirect(reverse("listing", args=(id,)))
    
@login_required
def closed(request):
    bidder_listings = Listing.objects.filter(active=False, current_bidder=request.user)
    creator_listings = Listing.objects.filter(active=False, creator=request.user)
    isBidderListing = bool(bidder_listings)
    isCreatorListing = bool(creator_listings)
    return render(request, "auctions/closed.html", { 
        "isbidder": isBidderListing,
        "iscreator": isCreatorListing,
        "bidder_listings": bidder_listings,
        "creator_listings": creator_listings,
        "message": "You have not closed any listings yet :("
        })



@login_required
def comment(request, id):
    listing = get_object_or_404(Listing, pk=id)
    new_comment = Comment(listing=listing, commenter=request.user, comment=request.POST["comment"])
    new_comment.save()
    return HttpResponseRedirect(reverse("listing", args=(id,)))
