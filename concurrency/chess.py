#!/usr/bin/python3.6

from datetime import datetime
from time import sleep
from random import random, choice, seed

import asyncio


oponents = ["Alexis", "Jordan", "Charly"]
moves_per_game = 4
random_time = lambda x: round(random()*x, 2)
seed(42)

def choose_move():
    move = choice(("A","B","C","D","E"))
    return move

def sync_choose_move():
    delay = ramdom_time()
    sleep(delay)
    return choose_move()

def sync_play():
    before = datetime.now()
    for turn in range(moves_per_game):
        for op in range(oponents):
            my_move = sync_choose_move()
            op_move = sync_choose_move()
            print(f"SYNC {turn} vs {op}: {my_move}-{op_move}")
    after = datetime.now()
    return (after-before).total_seconds()


async def async_play():
    before = datetime.now()

    async def async_turn(turn, op):

        my_delay = random_time(2)
        await asyncio.sleep(my_delay)
        my_move = choose_move()
        print(f"Turn {turn} vs {op}: I took {my_delay} seconds: {my_move}")

        op_delay = random_time(5)
        await asyncio.sleep(op_delay)
        op_move = choose_move()
        print(f"Turn {turn} vs {op}: {op} took {op_delay} seconds: {op_move}")

    async def play_op(op):
        for turn in range(moves_per_game):
            await async_turn(turn, op)

    tasks = [play_op(op) for op in oponents]
    await asyncio.wait(tasks)

    after = datetime.now()
    return (after-before).total_seconds()

def test_async():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_play())
    print(result)

def test_sync():
    print(sync_play())

test_async()