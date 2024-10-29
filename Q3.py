#Q3 :- Write a Python program to find the area of a triangle.
#Code below :-
def triangle_area(base, height):
    return(base * height)/2 #formula for area of triangle
base =int(input("ENTER YOUR CHOICE:"))
height = int(input("ENTER YOUR CHOICE:"))
area = triangle_area(base,height) # calling of function.
print(f"The area of the triangle with base {base} and height {height} is {area}")
