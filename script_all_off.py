import asyncio
import os
import os
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
import login_cred


async def main():
    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(email=login_cred.EMAIL, password=login_cred.PASSWORD)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve all the MSS310 devices that are registered on this account
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_type="mss710")
    PLUG =  'mss710:3.0.0:3.1.6'
    if len(plugs) < 1:
        print("No MSS310 plugs found...")
    else:
        # Turn it on channel 0
        # Note that channel argument is optional for MSS310 as they only have one channel
        dev = plugs[0]
        # Update device status: this is needed only the very first time we play with this device (or if the
        #  connection goes down)
        await dev.async_update()

       # print(f"Turning on {dev.name}...")
       # await dev.async_turn_on(channel=0)
       # print("Waiting a bit before turing it off")
        #await asyncio.sleep(5)
        #print(f"Turing off {dev.name}")
        await dev.async_turn_off(channel=0)
        dev = plugs[1]
        # Update device status: this is needed only the very first time we play with this device (or if the
        #  connection goes down)
        await dev.async_update()
        await dev.async_turn_off(channel=0)

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()
'''
if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()'''