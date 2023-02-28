#decorators

def div_dec(func):

    def wrapper(a,b):
        if b>a :
            a,b = b,a
        return func(a,b)
    return wrapper

@div_dec
def div(a,b):
    print(a/b)

div(5,10)   