# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/12
describle:
"""
from models import Publisher
from django import forms
TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)
class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(),initial="Replacce with your feedback")
    sender = forms.EmailField(required=False)

    def clean_message(self):
        message = self.cleaned_data.get('message','')
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words")
        return message


PublisherForm = forms.fields_for_model(Publisher)