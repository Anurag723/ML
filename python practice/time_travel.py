import math

velocity = float(input("Enter the velocity:-"))
print ("Ship moving at",velocity,"% of speed of light.")

c= 299792458
v= velocity/100.0*c

factor = 1/math.sqrt(1-((v**2)/(c**2)))

shipwt = 70000*factor
print ("ship moving with weight of", shipwt)
print ("Alpha Centauri:",4.3/factor,"light years")
print ("Barnard’s Star:",6.0/factor,"Light Years")
print ("Betelgeuse (in the Milky Way):", 309/factor,"Light years")
print ("Andromeda Galaxy (closest galaxy):",2000000/factor, "Light years")