from django.contrib import admin

from .models import Listing, Bid, User, Comments, Category

# Register your models here.
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Category)
