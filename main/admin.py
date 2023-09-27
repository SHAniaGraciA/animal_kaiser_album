from django.contrib import admin
from main.models import Item

# Register your models here.
@admin.register(Item)

class Item(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'description',)
    list_filter = ('description'),