from django import forms
from .models import Customer

class Timeframe_form(forms.ModelForm):
    
    days = (
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
    )
    part_of_day = (
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
        ('EVENING', 'Evening')
    )
    
    available_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=days)
    #available_parts_day = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                      choices=part_of_day)
    
    class Meta:
        model = Customer
        fields = ['available_days']