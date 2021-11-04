import time
import script_on_mrss,script_off_mrss,script_all_off
import webbrowser
from meross_iot.http_api import main
from threading import Thread

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

def esco_di_casa():
    background_thread = Thread(target=tutto_spent)
    background_thread.start()

