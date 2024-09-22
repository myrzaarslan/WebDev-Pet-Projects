from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed", views.closed, name="closed"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("create", views.create, name="create"), 
    path("listing<int:id>", views.listing, name="listing"),
    path("add_wl<int:id>", views.add_wl, name="add_wl"),
    path("rem_wl<int:id>", views.rem_wl, name="rem_wl"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bid<int:id>", views.bid, name="bid"),
    path("close_auction<int:id>", views.close_auction, name="close_auction"),
    path("comment<int:id>", views.comment, name="comment")
]
