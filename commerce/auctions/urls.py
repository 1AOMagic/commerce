from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("display_category", views.display_category, name="display_category"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("addComment/<int:id>", views.new_comment, name="addComment"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("add/<int:id>", views.add, name="add"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("close/<int:id>", views.close, name="close")
]
