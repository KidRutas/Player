# How about I build my own MATH library?

def ssum(a, b):
    print(a + b)

# We have our sum function but now we want to add two Arrays indexes together

arr = [1,2,3]
arrint = [4,5,6]
num = ["","","","","","",""]

for i in range(3):
    arr[i] += arrint[i]
    print(arr[i])
    print(arr)
