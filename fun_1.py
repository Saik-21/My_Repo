sqr =  lambda x:x**2
def check_prime(n):
   res = True
   if n==2:
        return res
   elif n>2:
       for i in range(2,n):
           if n%i==0:
               res = False
               break
       return res
l1 = [i for i in range(1,7)]
l2 = [i for i in range(1,21)]

#The use of map method is mentioned below
print(list(map(sqr,l1)))

#this is the use of filter method
print(list(filter(check_prime,l2)))
