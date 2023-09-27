#Stuttering Function
def stutter(word =''):
    st = ''
    for i in range(len(word)):
        if i<2:
            st += word[i]
    return '{}...{}..{}'.format(st,st,word)
print(stutter(word = 'incredible'))   


