# Write a program to find biggest in 3 numbers using else if
# Code :-
# Input three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print(f"The biggest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The biggest number is {num2}")
else:
    print(f"The biggest number is {num3}")

