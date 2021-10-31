import time
import login_cred
from datetime import datetime
from threading import Thread
import RPi.GPIO as GPIO
import smtplib, ssl
from timeout import timeout

global stato
stato = False
global psa
psa = ''


def login(passw):
    if passw == login_cred.passw:
        print('correct')
        return True
    else:
        print('not correct')
        return False

def login1(passw):
    if passw == '0171':
        return True
    else:
        return False

def start():
    background_thread = Thread(target=not_at_home)
    background_thread.start() 

def send_email():
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = login_cred.sender_email
    receiver_email = login_cred.receiver_email
    password = login_cred.password
    message = f"""\
    Subject: AVVISO SICUREZZA

    Caro alby Qualcuno e entrato alle {current_time} Del {current_date} """

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

def controllo1(pss):
    x = login1(pss)
    if not x:
        return False
    else:
        return True

def approva(pss):
    global psa
    psa = pss
    return psa

def not_at_home():
    time.sleep(5)
    x = False
    global stato
    stato = False
    GPIO.setmode(GPIO.BOARD)
    buttonPin = 16
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        buttonState = GPIO.input(buttonPin)
        if buttonState == False and stato == False:
            x = controllo(psa)
            print(x)
            stato = True
            #time.sleep(3)
            if x:
                return True
        elif buttonState == False and stato == True:
            pass
        else:
            stato = False
            x = controllo1(psa)
            if x:
                return True