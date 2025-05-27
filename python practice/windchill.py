# WCT=35.74+0.6215⋅T−35.75⋅V**0.16+0.4275⋅T⋅V**0.16      t=wind temp    v=air speed


airtemp = float(input("air temp:"))
airspeed = float(input("wind velocity:"))

wct = 35.74+(0.6215*airtemp)-(35.75*(airspeed**0.16))+(0.4275*airtemp*(airspeed**0.16))

print(wct)