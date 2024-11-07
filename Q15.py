#Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers between 1 and 10 are:")
for number in range(1, 11):
    if is_prime(number):
        print(number, end=" ")
