from django.shortcuts import render
from .forms import ContactForm
from .models import Contact, News
from django.conf import settings
import requests
import smtplib, ssl
import json

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# Create your views here.

def home(request):
    news = News.objects.all()[:3]
    
    context = {
        'news':news
    }
    return render(request,'base/index.html', context)

def news(request):
    news = News.objects.all()[:6]
    
    context = {
        'news':news
    }

    return render(request,'base/news.html', context)

def about(request):
    return render(request,'base/about.html')

def legal(request):
    return render(request,'base/legal.html')

def contable(request):
    return render(request,'base/contable.html')


def startup(request):
    return render(request,'base/startup.html')


def tributaria(request):
    return render(request,'base/tributaria.html')





def create_contact(request):
    if request.is_ajax and request.method == "POST":
        port = 465  # For SSL
        smtp_server = ""
        sender_email = ""  # Enter your address
        receiver_email = ""  # Enter receiver address
        password = ''

        fullname = request.POST['fullname']
        msg = request.POST['message']
        number = request.POST['number']
        mail_user = request.POST['email']

        message = MIMEMultipart('related')
        message["Subject"] = "Solicitud Página Web"

        body = """
        Estimado Ignacio, el usuario """ + fullname + """
        Ha enviado el siguiente mensaje a través de la página web : 
        """ + msg + """ y sus datos de contactos son : """ + number + ' ' + mail_user + """
        ."""

        part = MIMEText(body,"html")
        message.attach(part)
        
        # captcha_token = request.POST.get('captcha_token', None)
        captcha_token = request.POST['g-recaptcha-response']

        if captcha_token:
            url = 'https://www.google.com/recaptcha/api/siteverify'
            cap_data = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': captcha_token
            }
            response = requests.post(url=url, data=cap_data)

            if response.status_code == 200:
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                        server.login(sender_email, password)
                        text = message.as_string()
                        server.sendmail(sender_email, receiver_email, text)
                else:
                    print('solicitud incorrecta')
                        
            else:
                print('Wrong captcha')
        else:
            print('Wrong captcha')

    return render(request,'base/base.html')            