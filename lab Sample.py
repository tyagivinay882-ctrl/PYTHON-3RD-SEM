#1 Given a list of integers, extract even numbers, calculate their squares, and then extract squares greater than 100.
#2 Given a list of strings, extract strings with length greater than 3 and convert them into uppercase.
#3 Write a program to extract numbers divisible by 2 or 3 and calculate their squares.
#4 Given a list of integers, add 10 to every element and then extract elements greater than 30.
#5 Write a program to extract negative numbers and convert them into their absolute values.
#6 Given a list of words, extract words ending with the letter 'n' and calculate their lengths.
#7 Write a program to extract numbers that are perfect squares from a given list.

#1
numbers = [2, 4, 6, 8, 10, 12]

even = [x for x in numbers if x % 2 == 0]
squares = [x**2 for x in even]
result = [x for x in squares if x > 100]

print("Even numbers:", even)
print("Squares:", squares)
print("Squares greater than 100:", result)

#2
words = ["cat", "apple", "dog", "banana", "sun"]

result = [x.upper() for x in words if len(x) > 3]

print(result)

#3
numbers = [2, 3, 5, 6, 8, 9, 10]

result = [x**2 for x in numbers if x % 2 == 0 or x % 3 == 0]

print(result)

#4
numbers = [10, 15, 20, 25, 30]

result = [x + 10 for x in numbers if x + 10 > 30]

print(result)

#5
numbers = [-5, 10, -8, 15, -3]

result = [abs(x) for x in numbers if x < 0]

print(result)

#6
words = ["lion", "tiger", "hen", "elephant", "pen"]

result = [len(x) for x in words if x.endswith('n')]

print(result)

#7
numbers = [4, 9, 10, 16, 20, 25, 30, 36]

result = [x for x in numbers if int(x**0.5)**2 == x]

print(result)
