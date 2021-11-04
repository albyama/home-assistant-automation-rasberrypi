from tkinter import *
import secur,domotica
import controllo
from threading import Thread

def canc():
    global numero
    numero = ""

def press(num):
    global numero
    numero = numero + str(num)
    codice.set(numero)

def ok():
    x = numero
    secur.approva(x)
    y = secur.login1(x)
    if y:
        newwindow.destroy()
        domotica.letto_on()
        domotica.scrivania_on()

def go():
    secur.psa = ''
    secur.start() 

def pwindow():
    global newwindow
    newwindow = Toplevel(app)
    newwindow.title('Password Bitte')
    newwindow.geometry('800x480')
    newwindow.overrideredirect(True)
    newwindow.config(cursor='none')
    b1 = Button(newwindow,text='1',command=lambda: press(1),height = 5, width = 10).grid(column=0, row=0,sticky='new')
    b2 = Button(newwindow,text='2',command=lambda: press(2),height = 5, width = 10).grid(column=1, row=0,sticky='new')
    b3 = Button(newwindow,text='3',command=lambda: press(3),height = 5, width = 10).grid(column=2, row=0,sticky='new')
    b4 = Button(newwindow,text='4',command=lambda: press(4),height = 5, width = 10).grid(column=0, row=1,sticky='new')
    b5 = Button(newwindow,text='5',command=lambda: press(5),height = 5, width = 10).grid(column=1, row=1,sticky='new')
    b6 = Button(newwindow,text='6',command=lambda: press(6),height = 5, width = 10).grid(column=2, row=1,sticky='new')
    b7 = Button(newwindow,text='7',command=lambda: press(7),height = 5, width = 10).grid(column=0, row=2,sticky='new')
    b8 = Button(newwindow,text='8',command=lambda: press(8),height = 5, width = 10).grid(column=1, row=2,sticky='new')
    b9 = Button(newwindow,text='9',command=lambda: press(9),height = 5, width = 10).grid(column=2, row=2,sticky='new')
    b0 = Button(newwindow,text='0',command=lambda: press(0),height = 5, width = 10).grid(column=0, row=3,sticky='new')
    bok = Button(newwindow,text='ok',command=ok,height = 5, width = 10).grid(column=1, row=3,sticky='new')
    bcanc = Button(newwindow,text='canc',command=canc,height = 5, width = 10).grid(column=2, row=3,sticky='new')
    start = Button(newwindow,text='In sicurezza',command=go,height = 5, width = 10).grid(column=0, row=4,sticky='new')

app = Tk()
#inizio_controllo()
app.title('control pannel')
app.geometry('800x480')
app.config(cursor='none')
global codice
global numero
numero = ''
codice = StringVar()
scrivania_acceso = Button(text='Accendi scrivania',command=domotica.scrivania_on,height = 10, width = 20).grid(column=0, row=0,sticky='new')
scrivania_spento = Button(text='spegni scrivania',command=domotica.scrivania_off,height = 10, width = 20).grid(column=1, row=0,sticky='new')
letto_acceso = Button(text='Accendi letto',command=domotica.letto_on,height = 10, width = 20).grid(column=0, row=1,sticky='new')
letto_spento = Button(text='spegni letto',command=domotica.letto_off,height = 10, width = 20).grid(column=1, row=1,sticky='new')
tutto_spento = Button(text='spegni tutto',command=domotica.tutto_spent,height = 10, width = 20).grid(column=2, row=1,sticky='new')
via = Button(text='esco di casa',command=pwindow,height = 10, width = 20).grid(column=3, row=0,sticky='new')
musica = Button(text='spegni letto',command=domotica.music,height = 10, width = 20).grid(column=2, row=0,sticky='new')
app.mainloop()