def counter(func):
    def wrap(*args, **kwargs):
        wrap.count += 1
        print("{0} была вызвана: {1} раз(а)".format(func.__name__, wrap.count))
        return func(*args, **kwargs)
    wrap.count = 0
    return wrap

@counter
def foo():
    return None

for i in range(5):
    foo()
