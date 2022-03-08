from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import HomeView, EventView, EventDetailView, EventBookingView, BookedEventView, UserBookedEvents
app_name = 'event'

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('event', EventView.as_view(), name='events'),
    path('event/<slug>/', EventDetailView.as_view(), name='event_detail'),
    path('event-booking', EventBookingView.as_view(), name='event_book'),
    path('tickets-booked', BookedEventView.as_view(), name='tickets_booked'),
    path('view-booked-events', UserBookedEvents.as_view(), name='view-events'),
]
