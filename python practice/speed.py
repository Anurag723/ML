mph = float(input("Enter the speed in mph:-"))
meterph = mph*1609.34
bpd = meterph*24*117.647
fpf = mph*1760*24*14/220
mach = mph*5280/(1130*3600)
print(mach,"Speed in mach")
print(meterph,"Speed in meterph")
print(bpd,"Speed in berlyon per day")
print(fpf,"Speed in fulong per fortnight")