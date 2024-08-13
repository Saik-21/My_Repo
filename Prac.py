'''class Method:
        t = self.str.split(' ')
        j = t[::-1]
        j = ' '.join(j)
        return j

m1 = Method()
m1.str = "hello .py"
print(m1.rev())'''

'''class Circle:
    pi = 22/7

    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return self.pi*(self.radius**2)

c1 = Circle(14)
d1 = c1.__dict__
print(d1)'''


'''def factorial(t):
    if t==0:
        return 1
    else:
        return t*factorial(t-1)


def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        flag = True
        for i in range(2,n):
            if n%i==0:
                flag = False
        return flag



l = [i for i in range(1,10)]

#map according to the term makes sure that every element present in the list computed and then returned.
k = list(map(factorial,l))

f = [k for k in range(1,101)]
#filter is the function where it validates each element whether the function works on that element or not,
#It only returns the function that validates the function 
result = list(filter(is_prime,f))


#This is the reduce function where all the elements gets computed according to the function and result
from functools import reduce

t = lambda x,y:x+y

numbers = [1,2,3,4,5]
#Here we just get one single result, We need to import the function from the functools library
sum = reduce(t,numbers)
print(sum)'''


print(chr(97))
