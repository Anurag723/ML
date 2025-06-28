size = int(input("Enter the size of array:-"))
arr = []

for i in range(size):
    arr.append(int(input()))

pos = int(input("Enter the pos:-"))

res = (arr[pos]-arr[pos-1])-(arr[pos+1]-arr[pos])
print(res)