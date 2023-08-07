import dataclasses , csv
from django.shortcuts import render ,  get_object_or_404
from django.http import HttpResponse 
from django.core.mail import EmailMultiAlternatives
from sampark.settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail
from django.core.mail import  send_mail
from django.core.mail import EmailMessage
from .models import Email
from .forms import EmailForm
from django.core import mail

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_list = form.cleaned_data['email_list']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Convert email_list to a list
            email_list = email_list.split(',')

            # Send emails
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=email_list,
                fail_silently=False,
            )

            return render(request, 'email.html')
    else:
        form = EmailForm()

    return render(request, 'email.html', {'form': form})



# def emailcsv(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = form.cleaned_data['csv_file']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             recipients = []

#             for line in csv_file:
#                 email = line.decode('utf-8').strip()
#                 recipients.append(email)

#             send_mail(
#                 subject=subject,
#                 message=message,
#                 from_email=EMAIL_HOST_USER,
#                 recipient_list = recipients,
#                 fail_silently=False)

#             # print('list', recipient_list)

#             return render(request, 'email_csv.html')
#     # else:
#     #     form = EmailForm()

#     return render(request, 'email_csv.html')






def template(request):
 if request.method == 'POST':
    email1= request.POST.get('email1')
    email2= request.POST.get('email2')
    email3= request.POST.get('email3')
    email4= request.POST.get('email4')
    email5= request.POST.get('email5')
    email6= request.POST.get('email6')

    message1 = ('subject1', 'this is an email 1 message' , EMAIL_HOST_USER , [email1])
    message2 = ('subject2', 'this is an email 2 message' , EMAIL_HOST_USER , [email2])
    message3 = ('subject3', 'this is an email 3 message' , EMAIL_HOST_USER , [email3])
    message4 = ('subject4', 'this is an email 4 message' , EMAIL_HOST_USER , [email4])
    message5 = ('subject5', 'this is an email 5 message' , EMAIL_HOST_USER , [email5])
    message6 = ('subject6', 'this is an email 6 message' , EMAIL_HOST_USER , [email6])




    send_mass_mail((message1, message2, message3 , message4, message5 , message6), fail_silently=False)
 return render(request, 'template.html')

