num = int(input("Number given by the user:-"))
temp = num
rev = 0

while(temp!=0):
    rev = rev*10+(temp%10)
    temp = temp//10

dif = abs(num-rev)
temp = dif
rdif = 0

while(temp!=0):
    rdif = rdif*10+(temp%10)
    temp = temp//10

print(f"Reverse of the number is:{rev}")
print(f"Difference of the rev and num is:{dif}")
print(f"Reverse of difference is:-{rdif}")
print(f"Sum of dif and rdif is:{dif+rdif}")