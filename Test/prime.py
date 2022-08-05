n = int(input("Enter a number"))
flag = False
for i in range(int(n/2)):
    if (i != 0 and i != 1):
        if(n == 0 or n == 1):
            print("NOt Prime")
        else:
            if(n % i == 0):
                print("Else", i)
                flag = True
                break
if (flag == False):
    print("Number is Prime")
elif(flag == True):
    print("Number is not Prime")
