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


