from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def whtsp(request):
    return render(request,"whatsapp.html")


def Whatsapp(Num,Msg):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = "+91"+Num
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Msg)
    time.sleep(20)
    pg.press('enter')

def SendData(request):
    if request.method == 'POST':
        Num = request.POST['Phone']
        Msg = request.POST['Message']
        Whatsapp(Num,Msg)
        info = "Message has successfully sent.."
        return render(request,"whatsapp.html",{'info':info})
        
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")
