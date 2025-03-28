#userdefined
def well_wishes():
  print("Hi, How are you doing ?")

well_wishes()
well_wishes()
well_wishes()


def weather_condition():
  print("weather is pleasent in",spring)
  print("weather is same in",autumn)

spring="cool season"
autumn="winter"
weather_condition()


def add(P, Q):
   return P+Q

def subtract(P, Q):
  return P - Q

def multiply(P, Q):
  return P * Q

def divide(P, Q):
 return P / Q
# Now we will take inputs from the user
print("Please select operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/b/c/d):")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
  print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
  print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
  print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
  print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
  print("This is an invalid input")


#act4
def square_peri(x):
  perimeter=4*x
  print("perimeter of square is",perimeter)

def rectangle_peri(l,b):
  perimeter = 2*(l+b)
  return perimeter

def circumference(r):
  c=2*3.14*r
  print("circumference of circle is",c)

r=int(input("enter radius of circle:"))
circumference(r)

x=int(input("Enter side of square :"))
square_peri(x)

l = int(input("Enter length of rectangle->"))
b = int(input("Enter breadth of rectangle->"))
print(rectangle_peri(l,b))

#act5
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

# Adding a newline after each binary conversion for clarity
print("Binary of 7:", end=' ')
DecimalToBinary(7)
print()  # Newline

print("Binary of 15:", end=' ')
DecimalToBinary(15)
print()  # Newline

print("Binary of 3:", end=' ')
DecimalToBinary(3)
print()  # Newline



#ACP

import math

radius = float (input("enter the radius of a circle:"))

circumference= 2*math.pi* radius
print("circumference of a circle is :%.2f "% circumference)

