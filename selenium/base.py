import array

arr=array.array('l', [7, 8, 9, 4, 5, 78, 45, 98, 65, 32, 45, 85, 5])

print("the new array created is ",end=" ")
for l in range(0,13):
    print(arr[l],end=" ")
print("\r")
arr.append(3);

print("the appendedd array is",end=" ")
for l in range(0,14):
    print(arr[l],end=" ")


print("\r")

arr.insert(2,15)
print("\r")

print("the array after insertion is",end=" ")
for l in range(0,15):
    print(arr[l],end=" ")