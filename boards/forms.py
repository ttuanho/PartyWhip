from django.forms import ModelForm
from django import forms

from boards.models import Post, Bid


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'event_date': DateInput(),
            'end_date': DateInput(),
        }
        exclude = ('pub_date', 'winnerSelected',)


class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ('user',)
