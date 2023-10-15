#decorator is like a nextension to a function to modigy some changes to a function without causing any affect on the original function.
#Example
def exten(func):
    def wrap(n):
        lst = []
        for i in range(1,n+1):
            if i%2!=0:
                lst.append(i)
        print(f"odd list is {lst}")
        func(n)
    return wrap
    
@exten
def is_even(n):
    list = []
    for i in range(1,n+1):
        if i%2==0:
            list.append(i)
    print(f"Even list is {list}")

@exten
def is_three(n):
    list = []
    for i in range(1,n+1):
        if i%3==0:
            list.append(i)
    print(f"Multiples of 3:{list}")


