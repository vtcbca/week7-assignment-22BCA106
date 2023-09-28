#1.Write a Python script to enter an y number and check its prime or not
def primeornot(a):
    ans=True
    for i in range(2,a):
        if(a%2==0):
            ans=False
    if(ans==True):
        print("Number is prime!!")
    else:
        print("Number is not prime!!")


num=int(input("Enter a number:"))
primeornot(num)