#bubble sort
def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    return n

l = [6,9,1,4,5]
print(bubble_sort(l))