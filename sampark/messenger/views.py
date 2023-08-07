import csv
from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings
from .forms import SmsForm


def messenger(request):
    return render(request, "messenger.html")


def sendsms(request):
    numbers_list = []
    if request.method == 'POST':
        numbers = request.POST.get('phone_number')
        # numbers_list = numbers.split(',')
        message = request.POST.get('message')

        if not numbers or not message:
             return render(request,"messenger.html")

        if numbers:
            numbers_list = numbers.split(',')

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        for number in numbers_list:
            client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=number.strip()  # Remove any whitespace from the phone number
            )

        # return HttpResponse("SMS sent successfully!")
        return render(request, 'msg_comma.html')

    return render(request,"msg_comma.html")


def sendsmscsv(request):
    if request.method == 'POST'  and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        message = request.POST['message']
        # print(request.Files)

        # Read phone numbers from the CSV file
        phone_numbers = []
        for line in csv_file:
            phone_numbers.append(line.decode('utf-8').strip())

        # Initialize Twilio client with your credentials
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send SMS to each phone number
        for phone_number in phone_numbers:
            try:
                client.messages.create(
                    to=phone_number,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=message
                )
            except Exception as e:
                # Handle any errors that may occur during SMS sending
                print(f"Error sending SMS to {phone_number}: {str(e)}")

        # return HttpResponse("SMS sent successfully!")
        return render(request, 'msg_csv.html')

    return render(request, 'msg_csv.html')