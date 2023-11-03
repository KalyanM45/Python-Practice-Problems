def binary_search(list,key):
    low,high = 0, len(list)-1
    while low<=high:
        mid = (low+high)//2
        if list[mid]==key:
            return mid
        elif list[mid]<key:
            low=mid+1 
        elif list[mid]>key:
            high=mid-1
    return "Not Found"

list = [0,11,32,45,67,87,99]
key = 870
print(binary_search(list,key))