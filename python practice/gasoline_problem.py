ltr = float(input("Enter fuel in liters:-"))
gallon = ltr/3.7854
barrel = gallon/19.5
co2 = gallon*20
ethunit = gallon*75.700
cost = 4*gallon


print("Gallon produced:-", gallon)
print("barrel:-",barrel)
print("co2:-",co2)
print("Ethanol:-",ethunit)
print("Bill:-",cost)