# What is concurrency?

Concurrency is...

> [Oxford](https://www.lexico.com/en/definition/concurrence): The fact of two or more events or circumstances happening or existing at the same time.

> [Wikipedia](https://en.wikipedia.org/wiki/Concurrency_(computer_science)): The ability of different parts or units of a program, algorithm, or problem to be executed out-of-order or in partial order, without affecting the final outcome.

> [@tiangolo](https://fastapi.tiangolo.com/async/#asynchronous-code): Asynchronous code just means that the language has a way to tell the computer / program that at some point in the code, he will have to wait for something else to finish somewhere else. Let's say that something else is called "slow-file".

## When is concurrency useful?

There are many use cases for concurrency. The general rule would be to consider concurrency when in your code you need to execute functions that take a significant amount of time to complete and it would idle your program while waiting. Most times, these are I/O (input/output) operations as asking for a remote resource on the web.

## When is concurrency __not__ useful?

This of course depends on the problem you're trying to solve, but these are some cases where you should probably not use concurrency:

- your problem internally requires high CPU usage
- you don't need to reduce the amount of time your program takes to run

## Concurrency example: Chess Exhibition

OK, so now that you have an idea of what concurrency means, let's reinforce these concepts with an example:

One popular way to practice chess is by a simultaneous exhibition (simul). 
This means that an experienced player (master) plays multiple games at the same time with a number of other players.
Here, _at the same time_ means that the master will go from board to board choosing the next move and the other players will be waiting for him to continue the game, while thinking their next move.

So, let's say there are 4 players and a master for this particular exhibition.
Let's also say that each player has 90 seconds to decide the next move, the master 30 seconds and, for the sake of simplicity, they will always take that time. Finally, let's asume that each game takes 30 moves in total.

Given these asumptions, let's compare our simultaneous exhibition against playing sequentially (the master plays with each player until the game is finished and then goes on with the next).

- _Secuential exhibition_: 
   
      (30+90=120) seconds [thinking] * 15 [moves] * 4 [games] = 120 minutes total

- _Simultaneous exhibition_: the players will think their move while the master is away in another game, so we don't need to count those seconds

       30 seconds [thinking] * 15 [moves] * 4 [games] = 30 minutes total

__You'll find an implemention of this solution using python at [chess.py](https://github.com/unmateo/about-python/blob/develop/concurrency/chess.py)__

## How is concurrency implemented on python?

I'm not gonna dive deep into low level definitions nor advanced use cases. Instead, I'll describe some of the tools that the language provides and hopefuly will help you understand what kind of problems you'll be able to solve with them.

### asyncio module

This is the official module to handle concurrency. In was included into the Python Standard Library on version 3.4 (March 2014) and previously discussed on [PEP 3156] (https://www.python.org/dev/peps/pep-3156/) since 2012.

Since its release it suffered several modifications and improvements, so capabilities will depend on which version you are running.


### async/await keywords

These two keywords where discussed on [PEP 492] (https://www.python.org/dev/peps/pep-0492/) during 2015 and introduced on Python 3.5 (September 2015). They aim to provide a clear and easy way to handle concurrency and where made reserved words on Python 3.7 (June 2018).

```async def foo()``` will tell python that foo is an async function and it should be called with the await keyword.

```await foo()``` is the way of invoking an async function. This tells python that while executing foo, an await instruction might appear and the execution should continue instead of waiting for it.

Here's a short but quite complete example using python 3.6:

```python
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
```
---
Thanks for reading!