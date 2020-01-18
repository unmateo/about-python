#!/usr/bin/python3.6

from datetime import datetime
from time import sleep
from random import choice

import asyncio


oponents = (
    ("P1", "31"),
    ("P2", "32"),
    ("P3", "33") 
)
moves_per_game = 15
master_move_seconds = 0.3
player_move_seconds = 0.9


def move(player, color):
    move = choice(("A","B","C","D","E"))
    print(f'\x1b[6;{color};40m' + f'{player}: {move}' + '\x1b[0m')


def sync_play():
    print("Playing SYNC")
    before = datetime.now()
    for op, color in oponents:
        for turn in range(1, moves_per_game+1) :
            sleep(master_move_seconds)
            move(f"T{turn} - Master", color)
            sleep(player_move_seconds)
            move(f"T{turn} - {op}", color)
    seconds = (datetime.now()-before).total_seconds()
    print(f"SYNC game took {seconds} seconds")


async def async_play():
    before = datetime.now()

    async def async_turn(turn, op_tuple):
        op, color = op_tuple

        sleep(master_move_seconds)
        move(f"T{turn} - Master", color)

        await asyncio.sleep(player_move_seconds)
        move(f"T{turn} - {op}", color)

    async def play_op(op):
        for turn in range(1, moves_per_game+1):
            await async_turn(turn, op)

    tasks = [play_op(op) for op in oponents]
    await asyncio.wait(tasks)

    seconds = (datetime.now()-before).total_seconds()
    print(f"ASYNC game took {seconds} seconds")

def play(mode):
    if mode == "async":
        asyncio.get_event_loop().run_until_complete(async_play())
    elif mode == "sync":
        sync_play()

play("sync")
