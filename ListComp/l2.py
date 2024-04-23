#Here are some examples of list comprehensions in Python, starting from simple and progressing to more complex:

#Simple list comprehension:
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  

#List comprehension with a condition:
numbers = [1, 2, 3, 4, 5]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares) 

#List comprehension with a nested loop:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  

#List comprehension with multiple conditions:
numbers = [1, 2, 3, 4, 5]
even_squares_under_20 = [x**2 for x in numbers if x % 2 == 0 and x**2 < 20]
print(even_squares_under_20)  

#List comprehension with a function call:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = [x for x in numbers if is_prime(x)]
print(primes)  

#List comprehension with a lambda function:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  

#List comprehension with a dictionary:
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [25, 30, 35, 40]
people = [{'name': name, 'age': age} for name, age in zip(names, ages)]
print(people)
