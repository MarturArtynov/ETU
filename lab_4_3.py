import time

def bench(func):
    def wrap(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        print("{} выполнялась {} секунд".format(func.__name__, time.clock() - start))
        return result
    return wrap

@bench
def big_func(num):
    return num ** 10000

big_func(5000)
