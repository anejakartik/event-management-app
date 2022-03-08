from django.contrib import admin
from .models import Event, Slide, Booked_Event
admin.site.site_header = 'Event Management Admin'
# Register your models here.

def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'

class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'max_available_seats',
        'no_of_ticket_sold',
        'is_active',
    ]
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']
    prepopulated_fields = {"slug": ("title",)}
    actions = [copy_items]


class BookedEventAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'booked_date',
        'no_of_tickets',
        'event',
        'total_price',
    ]
    list_filter = ['user', 'event','booked_date']
    search_fields = ['user', 'event']

admin.site.register(Event, EventAdmin)
admin.site.register(Slide)
admin.site.register(Booked_Event, BookedEventAdmin)
