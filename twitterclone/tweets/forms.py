from django import forms


class AddTweetForm(forms.Form):
    body = forms.Charfield(widget=forms.Textarea)
