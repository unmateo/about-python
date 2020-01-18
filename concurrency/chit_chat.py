#!/usr/bin/python3.6
import asyncio

async def make_cofee():
    print(f"I'll make some coffee while we talk...")
    await asyncio.sleep(3)
    print("Oh, here's your coffee!")

async def chit_chat():
    print("Tell me something about yourself")
    await asyncio.sleep(2)
    print("Ha! That's very interesting.")
    print("What do you think about python?")
    await asyncio.sleep(2)
    print("I know, python's the best!")

loop = asyncio.get_event_loop()
tasks = asyncio.gather(make_cofee(), chit_chat())
loop.run_until_complete(tasks)
loop.close()
