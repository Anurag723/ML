yrs = int(input("How many years:-"))
fxpop = 307357870
time = 365*24*60*60
birth = time/7
death = time/13
immi = time/35

population_change = birth - death + immi

print("The estimated population in", yrs, "years is", int(population_change))