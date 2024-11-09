#Q1-: How to iterate through a list using for loop.
#Code :-
Names = ["Udit", "Charlie", "Delta"]
for Names in Names:
    print(Names)

#Q2 -:Sum of All Elements Write a function that takes a list of integers and returns the sum of all elements in the list.
#code :-
def sum_of_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 6, 8, 4, 5]
print("Sum of all elements:", sum_of_elements(numbers))

#Q3-:Find the Largest Element. Write a function that finds and returns the largest element in a list of integers.

#Q4-: Reverse a List. Write a function that takes a list and returns it in reverse order without using built-in reverse functions.
#code :-
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
numbers = [1, 7, 5, 8, 4]
print(reverse_list(numbers))

#Q5 -:Check for Duplicates . Write a function that checks if there are any duplicate values in a given list. Count Occurrences of an Element.
#code :-
def check_duplicates(lst):
    element_counts = {}
    has_duplicates = False
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
            has_duplicates = True
        else:
            element_counts[element] = 1

    return has_duplicates, element_counts
numbers = [1, 3, 6, 8, 4, 2, 9]
has_duplicates, element_counts = check_duplicates(numbers)
print("Has duplicates:", has_duplicates)
print("Element counts:", element_counts)




