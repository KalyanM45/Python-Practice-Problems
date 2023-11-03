def linear_search(list, key):
    for i in range(len(list)):
        if list[i]==key:
            return i
        
list = [1,2,3,4,5,6]
key = 5
print(linear_search(list, key))
