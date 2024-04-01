#bubble sort
def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    return n


#Insertion Sort
def insertion_sort(n):
    for i in range(1,len(n)):
        for j in range(i-1,0,-1):
            if n[j]>n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
            else:
                break
    return n



            