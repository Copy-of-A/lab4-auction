from django.contrib import admin
from .models import Auction, Category, Lot

# Register your models here.
# admin.site.register(Auction)
# admin.site.register(Category)
# admin.site.register(Lot)


# admin.site.register(Auction, AuctionAdmin)
@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'duration', 'category')
    list_filter = ('category', )


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('name', 'auction', 'start_price', 'start_time', 'seller')
    list_filter = ('auction', 'seller', 'is_sold')


