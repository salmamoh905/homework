# write a program to convert a users input from kgs to ibs and vicersa
weight=int(input("weight: "))
unit=input("(L)bs or(K)g: ")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are{converted}kilos")
else:
    converted=weight/0.45
    print(f"you are{converted}pounds")

# loops
total=[10,30,50]
print(sum(i for i in total))
