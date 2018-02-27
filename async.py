import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.gather(say('first hello', 2), say('second hello', 1)))

loop.close()