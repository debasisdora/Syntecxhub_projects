def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("can't divide by zero")
        return     
    return a/b
while True:
    print("simple_calculater*****")
    print("sum: 1")
    print("subsraction: 2")
    print("multiplication: 3")
    print("division: 4")
    print("Exit: 5")
    chose=int(input("chose a number: "))
    if chose==5:
        print("thanks for using the calculater")
        break
    elif chose in [1,2,3,4]:
        num1=float(input("enter 1st number:"))
        num2=float(input("enter 2nd number"))
        if chose==1:
            print("result: ",add(num1,num2))
        elif chose==2:
            print("result: ",sub(num1,num2))
        elif chose==3:
            print("result: ",mul(num1,num2)) 
        else:
            print("result: ", div(num1,num2))  
    else:
        print("invalid number")    
            # Syntecxhub_simple_calcularter