from django import forms


class BookingForm(forms.Form):
    event_id = forms.IntegerField()
    tickets = forms.IntegerField()
