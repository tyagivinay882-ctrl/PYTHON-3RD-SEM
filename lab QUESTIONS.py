#1
num = int(input("Enter a number: "))
for i in range(1, 11):
  print(num, "x", i, "=", num * i)

#2
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
  print("*" * i)

#3
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
  spaces = " " * (rows - i)
  stars = "*" * (2 * i - 1)
  print(spaces + stars)

#4
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
  factorial = factorial * i
  print("Factorial =", factorial)

#5
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
  print(a, end=" ")
  c = a + b
  a = b
  b = c

#6
num = int(input("Enter a number: "))
if num <= 1:
  print("Not a prime number")
else:
  is_prime = True
  for i in range(2, num):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
        print("Prime number")
  else:
        print("Not a prime number")



  