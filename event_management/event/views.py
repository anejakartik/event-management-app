from turtle import title
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Event, Booked_Event
from .forms import BookingForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(View):

    def get(self, *args, **kwargs):
        events = Event.objects.filter(is_active=True)
        context = {
                    'events' : events
                    }

        if self.request.user.is_authenticated:
            return render(self.request, 'index.html',context=context)
        else:
 
            return render(self.request, 'index.html',context=context)

class EventView(ListView):
    model = Event
    paginate_by = 6
    template_name = "event.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "event-detail.html"


class EventBookingView(LoginRequiredMixin, View):
    
    def post(self, *args, **kwargs):
        Booking = BookingForm(self.request.POST or None)
        if Booking.is_valid():
           try:
               event_id = Booking.cleaned_data.get('event_id')
               quantity = Booking.cleaned_data.get('tickets')
               event =  Event.objects.filter(id=event_id)
               if event:
                   context = {
                       'events' : event[0],
                       'quantity' : quantity
                       }
                   return render(self.request, 'booking_summary.html',context=context)
           except ObjectDoesNotExist:
                messages.error(self.request, "Invalid Event")
                return redirect("/")




class BookedEventView(View):

    def post(self, *args, **kwargs):
        Booking = BookingForm(self.request.POST or None)
        if Booking.is_valid():
            event_id = Booking.cleaned_data.get('event_id')
            quantity = Booking.cleaned_data.get('tickets')
            event = Event.objects.filter(id=event_id)
            event = event[0]
            if event.max_available_seats < (quantity+event.no_of_ticket_sold):
                messages.error(self.request, "Sorry no of seats selected are not available at the moment.")
                return redirect("/")
            else:
                event.no_of_ticket_sold = event.no_of_ticket_sold + quantity
                event.save()
                print(self.request.user)
                confirm_booking = Booked_Event.objects.create(event=event,user=self.request.user,no_of_tickets=quantity,total_price =(quantity*event.price) )
                confirm_booking.save()
                messages.info(self.request, "Your Event booking is successfull.")
                return redirect("/")



class UserBookedEvents(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            events = Booked_Event.objects.filter(user=self.request.user).order_by('-booked_date')
            context = {
                        'events' : events
                        }
            return render(self.request, 'view_user_events.html',context=context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You havent booked any events yet.")
            return redirect("/")
