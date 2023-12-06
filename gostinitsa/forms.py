from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'duration']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['check_in_date'].widget.attrs.update(
            {'placeholder': 'Выберите дату заезда', 'class': 'form-control'})
        self.fields['duration'].widget.attrs.update(
            {'placeholder': 'Введите продолжительность пребывания', 'class': 'form-control'})
