ipt = float(input("Enter the richter"))

po = (1.5*ipt)+4.8
eng = 10**po
tntpj = 4.184*(10**9)
tnt = eng/tntpj

print(eng," ",tnt)