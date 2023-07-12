sub1=int(input('Enter First SUBJECT mark:'))
suj2=int(input('Enter SECOND SUBJECT mark:'))
sub3=int(input('Enter THIRD SUBJECT mark:'))
suj4=int(input('Enter Fourth SUBJECT mark:'))
sub5=int(input('Enter FIFTH SUBJECT mark:'))
avg=int((sub1 + suj2 + sub3 + suj4 + sub5) / 5)

results = [sub1, suj2, sub3, suj4, sub5]
print(type(results))


if any([results<35 for results in results]):
   # print('na')
    print('you are fail')
    
    
if(avg>=90):
    print(avg)
    print("Grade A")
elif(avg>=80):
    print(avg)
    print("Grade B")
elif(avg>=70):
    print(avg)
    print("Grade C")
elif(avg>=60):
    print(avg)
    print("Grade D")
else:
    print(avg)
    print("Grade F")
    