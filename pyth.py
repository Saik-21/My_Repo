class dec_class(object):
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        print(f"call method is executed before is {self.func.__name__}")
        return self.func(*args,**kwargs)

@dec_class
def display_info(name,age):
    print(f'The display ran with {name} {age}')


display_info('Thomas',29)