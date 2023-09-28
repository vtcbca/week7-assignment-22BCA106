#2.Write a python script to enter any number and print the sum of its digit.

def sumofdigit(s):
    a=s
    ram=0
    sum=0
    while(s!=0):
        ram=s%10
        sum=sum+ram
        s//=10
    print(f"The sum of digit of number {a} is {sum}!")  

num=int(input("Enter a number:"))
sumofdigit(num)