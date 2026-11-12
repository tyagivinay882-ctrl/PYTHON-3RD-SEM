#1
numbers = []

print("Enter 10 numbers:")

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Even numbers:")

for n in numbers:
    if n % 2 == 0:
        print(n)

#2
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

numbers = list(set(numbers))
numbers.sort()

if len(numbers) >= 2:
    print("Second largest value:", numbers[-2])
else:
    print("Second largest value does not exist")

#3
subjects = []

print("Enter 5 subjects:")

for i in range(5):
    subject = input("Enter subject: ")
    subjects.append(subject)

subjects = tuple(subjects)

sub1, sub2, sub3, sub4, sub5 = subjects

print("Subjects after unpacking:")
print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)

#4
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

unique_numbers = set(numbers)

print("List after removing duplicates:")
print(unique_numbers)

#5
students = {}

print("Enter details of 5 students:")

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks:")

for name, marks in students.items():
    print(name, ":", marks)

#6
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")

for char, count in frequency.items():
    print(char, ":", count)


