from django import forms
class EmailForm(forms.Form):
    email_list = forms.CharField(label='Emails', widget=forms.Textarea(attrs={'placeholder': 'enter comma seperated mails to send mail to multiple user at once. eg- nanxxxxxxxx@gmail.com,sapxxxxxxx@gmail.com,asgxxxxx@gmail.com'}) )
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea,max_length = 300)
    # csv_file = forms.FileField(label='CSV File')

    