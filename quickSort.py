import random
import time
def quickSort(array,start,end):
    if start>=end:
        return
    pivot=findPivot(array,start,end)
    quickSort(array,start,pivot-1)
    quickSort(array,pivot+1,end)
def findPivot(array,start,end):
    left=start
    right=end
    while True:
        while left<end and  array[left]<=array[end]:
            left+=1
        if left==end:
            break
        while right>start and array[right]>=array[end]:
            right-=1
        if left<right:
            array[left],array[right]=array[right],array[left]
        else:
            array[end],array[left]=array[left],array[end]
            break
    return left
if __name__ == '__main__':
    array=[]
    for i in range(10000):
        array.append(random.randint(1,100000))
    print(time.time())
    quickSort(array,0,len(array)-1)
    print(time.time())

