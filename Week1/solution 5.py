#5.Write a python script to enter any string and count vowel.

def vowels(s):
    a=('a','e','i','o','u','A','E','I','O','U')
    vowel=0
    for i in s:
        if i in a:
            vowel+=1
    print(f"The vowels count in '{s}' is {vowel}")

s=input("Enter a string:")
vowels(s)    