import time
import RPi.GPIO as GPIO
import smtplib, ssl
from timeout import timeout

def login(passw):
    try:
        if passw == 'passwword':
            print('correct')
            return True
        else:
            print('not correct')
            return False
    except:
        pass


def send_email():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "your@email.com.com"
    receiver_email = "receiver@email.com"
    password = 'your_email_password'
    message = """\
    Subject: Hi there

    Qualcuno e eintrato alle """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
def controllo(pss):
    x = login(pss)
    if not x:
        send_email()
        return False
    else:
        print('welcome')
        return True

def not_at_home(pss):
    GPIO.setmode(GPIO.BOARD)
    buttonPin = 16
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        buttonState = GPIO.input(buttonPin)
        if buttonState == False:
            x = controllo(pss)
            print(x)
            return x
        else:
            pass