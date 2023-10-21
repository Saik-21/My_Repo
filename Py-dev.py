'''def logger(func):
    def log(*args):
        print(f"Using {func.__name__} with {args} we get:")
        print(func(*args))
    return log

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

mul_log = logger(mul)
sub_log = logger(sub)
mul_log(3,3)
mul_log(7,2)
sub_log(6,5)''' #This is a  n example of closure


'''def describe(func):
    def present(*args):
        print(f"the binary representation of function: {bin(*args)}")
        func(*args)
        print(f"the binary representation of function: {bin(func(*args))}")
    return present

@describe
def stat(x):
    x  = x << 2
    print(f"operation shift:{x}")
    return x

stat(6)'''

