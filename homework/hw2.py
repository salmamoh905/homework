# write a function to ask a user to enter the weight in pounds and return the weight converted into Kgs
# {is on its own}print a message that says you are{value}Kgs
# 1lb=0.45kg

def my_converter(kilogram, pound):
    weight=int(input("weight: "))
    unit=input("(L)bs or(K)g: ")
    if unit.upper()=="L":
       converted=weight*0.45
       print(f"you are{converted}kilos")
    else:
       converted=weight/0.45
       print(f"you are{converted}pounds")


# write a program that converts numerical digits to words 
# 123= one two three
# get users input 
# loop





#Program to input a number upto 5 digits and print it in words
number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=int(input("Enter a number "))
if n>99999:
    print("Cant solve for more than 5 digits")
else:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    num=""
    if d[4]!=0:
        if(d[4]==1):
            num+=tens[d[3]]+ " Thousand "
        else:
            num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "
    else:
        if d[3]!=0:
            num+=number[d[3]]+ " Thousand "
    if d[2]!=0:
        num+=number[d[2]]+" Hundred "
    if d[1] != 0:
        if (d[1] == 1):
            num += tens[d[0]]
        else:
            num += nty[d[1]] + " " + number[d[0]]
    else:
        if d[0] != 0:
            num += number[d[0]]
    print(num)





 


  




