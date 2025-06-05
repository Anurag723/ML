import math

sog = float(input("Enter the side of garden(feet):-"))
pdis = float(input("Enter the distance between plants(feet):-"))
dgs = float(input("Enter the depth of garden soil(feet):-"))
df = float(input("Enter the depth of fill(feet):-"))

aog = sog**2;
aofs = math.pi*((sog/4)**2)/2
aoc = aofs*2

pis = math.trunc(aofs/(pdis**2))
pic = math.trunc(aoc/(pdis**2))

tnp = pis*4+pic

sos = aofs*dgs*0.03703704           #0.03703704 is multiplied to make feet to yard
soc = aoc*dgs*0.03703704            #0.03703704 is multiplied to make feet to yard

twf = aog-(aofs*4+aoc)
tof = twf*df*0.03703704

print()
print(f"Number of plant in each semicircle flowerbed:{pis}")
print(f"Number of plant in each circle flowerbed:{pic}")
print(f"Number of plant flowerbed:{tnp}")

print()
print(f"soil for semicircle{sos:0.1f} cu. yards")
print(f"soil for circle{soc:0.1f} cu. yards")

print()
print(f"Total soil:{soc+(sos*4):0.1f} cu. yards")
print(f"Total fill is {tof:0.1f} cu. yards")