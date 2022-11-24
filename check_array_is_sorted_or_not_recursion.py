def sorted(arr):
    if len(arr)<=1:
        return True
    if arr[0]>arr[1]:
        return False
    return sorted(arr[1:])
    
    

def sort_check(arr,index):
    if index==len(arr)-1:
        return True
    return arr[index]<arr[index+1] and sort_check(arr,index+1)

print(sorted([1,3,5,10]))
print(sort_check([1,2,5,6],0))