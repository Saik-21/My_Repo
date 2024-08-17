#has33 problem
def has_33(l):
    for i in range(0,len(l)-1):
        if l[i]==3 and l[i+1]==3:
            return True
    return False
            
#paper_doll Problem
def paper_doll(s):
    res = ''
    for i in s:
        res+=i*3
    return res

#check whether there are harshad
def is_harshad(num):
    t = 0
    for i in str(num):
        t+=int(i)
    if num%t==0:
        return True
    return False

def summer_69(l):
    total = 0
    skip = True

    for num in l:
        while skip:
            if num!=6:
                total+=num
                break
            else:
                skip = False
        while not skip:
            if num!=9:
                break
            else:
                skip = True
                break
    return total

def check_prime(n):
    if n<=1 or n==2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def count_prime(n):
    count = [2]
    for i in range(3,n,2):
        for j in range(2,i):
            if i%j==0:
                break     
        else:
            count.append(i)
    return count


        
print(count_prime(100))
