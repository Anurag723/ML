dbtnum = int(input("Enter the debt number:-"))
dencurr = int(input("Enter the debt currency:-"))

height = (dbtnum/dencurr*0.0043)/63360
times = height/238857

print ("Denomination is:-",height)
print ("denomination is",times,"times the distance of earth to moon.")