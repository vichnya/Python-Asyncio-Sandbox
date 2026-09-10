# Примечание: При запуске кода могут возникнуть проблемы с библиотекой keyboard, Repl.it не может ее импортировать. В VS-code программа работает без проблем.

import asyncio
import datetime
from termcolor import cprint
import keyboard

async def display_time():
    try:
        while IsAlive:
            time_big = datetime.datetime.now().strftime("%Y-%m-%d")
            time_small = datetime.datetime.now().strftime("%H:%M:%S")
            cprint(time_big, "green", attrs=["bold"], end=' ')
            cprint(time_small, "red", attrs=["bold"])
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass

async def main():
    try:
        await asyncio.gather(display_time())
    except KeyboardInterrupt:
        pass

def Terminate():
  global IsAlive
  IsAlive = False


IsAlive = True
keyboard.add_hotkey('esc', Terminate)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass