import uvloop
import asyncio


#runs the given function with the arguments passed
def run_in_loop(func, *args, **kwargs):
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(func(*args, **kwargs))
    loop.close()
    return result
