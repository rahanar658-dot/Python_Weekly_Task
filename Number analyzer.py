def even_odd(n):
    if n %2==0:
        print("Even number")
    else:
        print("Odd numbers")
num=int(input("Enter a number:"))
even_odd(num)

def check_number(n):
    if n>0:
      print("Positive Number")
    elif n<0:
        print("Negative Number")
    else:
        print("Zero")
num=int(input("Enter a number:"))
check_number(num)

def square(n):
    print("Square=",n*n)
num=int(input("Enter a number:"))
square(num)
