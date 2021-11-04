from datetime import datetime
import time
import secur
import login_cred,domotica
from threading import Thread
import smtplib, ssl
from timeout import timeout
def temperatura():
    pass


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

    Caro alby porta ancora aperta alle {current_time} Del {current_date} """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def update_time():
    ora = datetime.now()
    ora = ora.strftime("%H:%M:%S")
    [h, m, s] = ora.split(':')
    x = int(h)
    y = int(m)
    z = int(s)
    ntime = f'{h}{m}{s}'
    xc = int(ntime)
    time.sleep(1)
    return ora

def still_open():
    while secur.ancora_aperto:
        time.sleep(20)
        send_email()


def inizio_controllo():
    background_thread = Thread(target=maino)
    background_thread.start()


def maino():
    while True:
        still_open()


