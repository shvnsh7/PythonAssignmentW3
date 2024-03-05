from time import time,sleep
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapped(*arg,**kwargs):
        start=time()
        res=func(*arg,**kwargs)
        end=time()
        print(f"{func.__name__} took {int(end-start)} seconds")
        return res
    return wrapped

@timeit
def myfunc(time_to_sleep:int)-> None:
    """This function does some work"""
    sleep(time_to_sleep)

@timeit
def myfunc2():
    return 1
    # print("hello")

myfunc=timeit(myfunc)

# myfunc(1)
ret=myfunc2()
print(ret)
myfunc2()

