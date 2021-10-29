from tkinter import *
from func import secur
from meross_iot.http_api import main
from func import script_on_mrss,script_off_mrss,script_all_off
import webbrowser

def scrivania_on():
    id = 1
    loop = script_on_mrss.asyncio.get_event_loop()
    task = loop.create_task(script_on_mrss.main(id))
    loop.run_until_complete(task)
    #loop.close()
def scrivania_off():
    id = 1
    loop = script_off_mrss.asyncio.get_event_loop()
    task = loop.create_task(script_off_mrss.main(id))
    loop.run_until_complete(task)
    #loop.close()
def letto_on():
    id = 0
    loop = script_on_mrss.asyncio.get_event_loop()
    task = loop.create_task(script_on_mrss.main(id))
    loop.run_until_complete(task)
    #loop.close()
def letto_off():
    id = 0
    loop = script_off_mrss.asyncio.get_event_loop()
    task = loop.create_task(script_off_mrss.main(id))
    loop.run_until_complete(task)
    #loop.close()
def tutto_spent():
    id = 0
    loop = script_all_off.asyncio.get_event_loop()
    task = loop.create_task(script_all_off.main())
    loop.run_until_complete(task)
def music():
    webbrowser.open("https://open.spotify.com/", new=1)
def canc():
    global numero
    numero = ""
def press(num):
    global numero
    numero = numero + str(num)
    codice.set(numero)
    print(codice)
def ok():
    x = numero
    y = secur.not_at_home(x)
    if y:
        newwindow.destroy()
        
def pwindow():

    global newwindow
    newwindow = Toplevel(app)
    newwindow.title('Password Bitte')
    newwindow.geometry('800x480')
    newwindow.overrideredirect(True)
    #secur.not_at_home("")
    b1 = Button(newwindow,text='1',command=lambda: press(1),height = 5, width = 10).grid(column=0, row=0)
    b2 = Button(newwindow,text='2',command=lambda: press(2),height = 5, width = 10).grid(column=1, row=0)
    b3 = Button(newwindow,text='3',command=lambda: press(3),height = 5, width = 10).grid(column=2, row=0)
    b4 = Button(newwindow,text='4',command=lambda: press(4),height = 5, width = 10).grid(column=0, row=1)
    b5 = Button(newwindow,text='5',command=lambda: press(5),height = 5, width = 10).grid(column=1, row=1)
    b6 = Button(newwindow,text='6',command=lambda: press(6),height = 5, width = 10).grid(column=2, row=1)
    b7 = Button(newwindow,text='7',command=lambda: press(7),height = 5, width = 10).grid(column=0, row=2)
    b8 = Button(newwindow,text='8',command=lambda: press(8),height = 5, width = 10).grid(column=1, row=2)
    b9 = Button(newwindow,text='9',command=lambda: press(9),height = 5, width = 10).grid(column=2, row=2)
    b0 = Button(newwindow,text='0',command=lambda: press(0),height = 5, width = 10).grid(column=0, row=3)
    bok = Button(newwindow,text='ok',command=ok,height = 5, width = 10).grid(column=1, row=3)
    bcanc = Button(newwindow,text='canc',command=canc,height = 5, width = 10).grid(column=2, row=3)
app = Tk()
app.title('control pannel')
app.geometry('800x480')
#app.config(cursor='none')
global codice
global numero
numero = ''
codice = StringVar()
scrivania_acceso = Button(text='Accendi scrivania',command=scrivania_on,height = 10, width = 20).grid(column=0, row=0)
scrivania_spento = Button(text='spegni scrivania',command=scrivania_off,height = 10, width = 20).grid(column=1, row=0)
letto_acceso = Button(text='Accendi letto',command=letto_on,height = 10, width = 20).grid(column=0, row=1)
letto_spento = Button(text='spegni letto',command=letto_off,height = 10, width = 20).grid(column=1, row=1)
tutto_spento = Button(text='spegni tutto',command=tutto_spent,height = 10, width = 20).grid(column=2, row=1)
via = Button(text='esco di casa',command=pwindow,height = 10, width = 20).grid(column=3, row=0)
musica = Button(text='spegni letto',command=music,height = 10, width = 20).grid(column=2, row=0)
app.mainloop()