#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

def armstong(s):
    s=int(s)
    rem=0
    sum=0
    a=s
    while(s!=0):
        rem=s%10
        sum=sum+(rem**3)
        s//=10
    if(a==sum):
        print(f"The number {a} is an armstrong number!")
    else:
        print(f"The number {a} is  not an armstrong number!")


num=input("Enter a number!!:")
if(num.isdigit()):
    armstong(num)
else:
    print(f"The given input {num} is not valid number!!")