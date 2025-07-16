def isAnnagram(val1:str, val2:str)->bool:
    rs1 = sorted(val1)
    rs2 = sorted(val2)

    return rs1==rs2

print(isAnnagram("racecar","carrace"))