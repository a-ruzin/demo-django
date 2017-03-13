from django.contrib import admin

from shop.models import Category, Item

admin.site.register(Category)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date', 'is_new')

admin.site.register(Item, ItemAdmin)

