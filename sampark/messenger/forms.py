from django import forms

class SmsForm(forms.Form):
    phone_number = forms.CharField(label='phone_number', widget=forms.Textarea)
    csv_file = forms.FileField()
    message = forms.CharField(label='Message', widget=forms.Textarea)


    