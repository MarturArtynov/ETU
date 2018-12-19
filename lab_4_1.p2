def TAG(tag):
    def decorator(func):
        def wrap(*args, **kwargs):
            return "<{}>".format(tag) + func(*args, **kwargs) + "<{}>".format(tag)
        return wrap
    return decorator

@TAG('b')
def make_bold(string):
    return string

@TAG('div')
def make_div(string):
    return string

print(make_div(make_bold('2')))
