import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from django.core.exceptions import ValidationError

from boards.models import Post, Bid

from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(ModelForm):

    # def is_valid(self):
    #     print("here")
    #     valid = super(PostForm.Meta, self).is_valid()
    #
    #     if not valid:
    #         return valid
    #
    #     if self.end_date >= self.event_date:
    #         return False
    #
    #     return True

    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #
    # def clean_end_date(self):
    #     end_date = self.cleaned_data['end_date']
    #     if end_date <= timezone.now():
    #         raise ValidationError("Please select a valid date")
    #     return end_date
    #
    # def clean_event_date(self):
    #     event_date = self.cleaned_data['event_date']
    #     if event_date <= timezone.now():
    #         raise ValidationError("Please select a valid date")
    #     return event_date
    #


    class Meta:
        model = Post
        widgets = {
            'event_date': DateInput(),
            'end_date': DateInput(),
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Enter your budget'}),
            'location': forms.TextInput(attrs={'placeholder':'Enter a suburb'}),
            'comment': forms.Textarea(attrs={'placeholder':'Extra information (e.g. number of guests, occasion, type of venue, cooking facilities)'}),

        }

        exclude = ('user', 'pub_date', 'winner_selected', 'status')




class BidForm(ModelForm):
    class Meta:
        model = Bid
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'Enter bid amount'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Enter extra information'}),
            'contact_details': forms.TextInput(attrs={'placeholder': 'Enter contact details'})
        }
        exclude = ('user', 'post')



SORT_BY= [
    ('most_recent', 'Most Recent'),
    ('budget_ascending', 'Budget (Ascending)'),
    ('budget_descending', 'Budget (Descending)'),
    ('event_date_descending', 'Event Date (Descending)'),
    ('event_date_ascending', 'Event Date (Ascending)'),
    ]

TIME_FILTER = [
    ('this_week', 'This Week'),
    ('this_month', 'This Month'),
]

def validate_positive(value):
    if value < 0:
        raise ValidationError('Enter positive Value')
    return value


class OptionsForm(forms.Form):
    sort_option = forms.ChoiceField(label = '', choices=SORT_BY, widget=forms.RadioSelect(attrs={'style' : 'margin-right: 10px'}), required=False)
    min_value = forms.FloatField(label = 'Min Budget', min_value=0, max_value=100000, required=False, validators=[validate_positive], widget=forms.TextInput(attrs={ 'class' : 'budgetRange'}))
    max_value = forms.FloatField(label = 'Max Budget', min_value=0, max_value=100000, required=False, validators=[validate_positive], widget=forms.TextInput(attrs={ 'class' : 'budgetRange'}))
    time_range = forms.ChoiceField(label = 'Date', choices=TIME_FILTER, widget=forms.RadioSelect(attrs={'style' : 'margin-right: 10px'}), required=False)
