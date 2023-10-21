'''class dec_class(object):
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        print(f"call method is executed before is {self.func.__name__}")
        return self.func(*args,**kwargs)

@dec_class
def display_info(name,age):
    print(f'The display ran with {name} {age}')


display_info('Thomas',29)'''

'''def dict(func):
    def wrap(st):
        print(f'String before:{st}')
        print(f'The String after Execution is {st.lower()}')
        return func(st)
    return wrap

@dict
def change(st):
    print(f'The String  at present is:{st.upper()}')

change('University')'''

class address:
    rent = 3000
    def __init__(self,H_no,colony_name,city):
        self.H_no = H_no
        self.colony_name = colony_name
        self.city = city
    
    def landmark(self,l):
        return f'The nearest landmark is {l}'
    
    
    '''Class method is a decorator implemented on a method which takes a class as an attribute and we can use that decorator as
    function enables the method changes the class  attribute define before creating an object'''
    @classmethod 
    def rent_raise(cls,amount):
        cls.rent = cls.rent + amount
    
owner_1 = address(23,'silverrain','Houston')
owner_1.landmark('leaf School')
address.rent_raise(500)
address.rent_raise(1000)
owner_2 = address(78,'Goldlane','Houston')
print(owner_2.landmark('Walmart'))
print(owner_1.__dict__)