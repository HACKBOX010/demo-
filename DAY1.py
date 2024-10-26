# code to print hello world
print("hello world")


#basic addition
#Q - Write a code for addition of two numbers.
a=int(input("enter your choice:"))
b=int(input("enter your choice:"))
print("sum:",a+b)

#basic subtraction
# Q - write a code for subtraction  two number.
a=int(input("enter your choice:"))
b=int(input("enter your choice:"))
print("difference",a-b)

#basic multiplication
# Q- Write a code for multiplication of two numbers.
a=int(input("enter your choice:")) #int is used for typecasting
b=int(input("enter your choice:"))
print("product",a*b)

#basic division
#Q - Write a code for division of two numbers.
a=int(input("enter your choice:"))
b=int(input("enter your choice:"))
print("division",a/b)

#check if its even or odd

def check_even_odd(number):
     if number % 2 == 0:
         return"even"
     else:
         return "odd"
num = int(input("enter a number:"))
result = check_even_odd(num)
print(result)

