import math

side = float(input("please enter the side length in feet "))
dst = float(input("enter the distance between plant in inches "))
dpt = float(input("deapth of flower bed in feet "))
dptf = float(input("Enter the depth to fill in feet "))

argar = side**2

bedar = ((side/2)**2)/2


# Convert plant spacing from inches to feet

dstft = dst/12
areaperplant = dstft**2

# center area of circle
carea = math.pi*((side/4)**2)

print("Plant per triangle",int(bedar/areaperplant))
print ("Plant in circle ",int(carea/areaperplant))

print("Summary of soil needed")

soilft = (bedar*dpt)/27
soilfc = (carea*dpt)/27

print(f"soil fill for triangle {soilft:.1f}")
print(f"soil fill for circle {soilfc:.1f}")

print(f"total soil needed {(soilft*4)+soilfc:.1f}")

farea = argar-carea-(bedar*4)
print(f"Fill needed {(farea*dptf)/27:.1f}")