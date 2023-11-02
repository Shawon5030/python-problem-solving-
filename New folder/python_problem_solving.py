#1. Write a program that swaps the values of two variables.
a=100
b=200

x=a
a=b
b=x
print('value of a=',a)
print('value of b=',b)

#2. Write a program that calculates the area of a rectangle given its length and width.
length=float(input(" enter the value of length"))
width=float(input(" enter the value of width"))

area_of_a_rectangle=(length*width)
print(area_of_a_rectangle)

#3. Write a program that converts temperature from Fahrenheit to Celsius.
Fahrenheit=float(input("enter thr value of Fahrenheit"))
Celsius=((Fahrenheit -32)*5)/9
print(Celsius)

#4. Write a program that calculates the volume of a sphere given its radius.
radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * 3.1416 * (radius ** 3)
print(volume)

#5. Write a program that finds the average of three numbers.
number_1=int(input("first number"))
number_2=int(input("second number"))
number_3=int(input("3rd number"))

average=(number_1+number_2+number_3)/3
print(average)

#6. Write a program that determines if a number is even or odd.
number=int(input('enter the number '))
if number%2==0:
    print("even")
else:
    print("odd")

#7. Write a program that finds the maximum of three numbers.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum
if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

print(maximum)
#8. Write a program that determines if a year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#9. Write a program that determines if a number is positive, negative, or zero.
number=int(input("enter your number"))
if number >0:
    print("positive")
elif number==0:
    print("zero")
else:
    print('negative')

## 10. Write a program that calculates the grade based on a given percentage.
percentage = float(input("Enter the percentage: "))


if percentage >= 90:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 80:
    grade = "A-"
elif percentage >= 75:
    grade = "B+"
elif percentage >= 70:
    grade = "B"
elif percentage >= 65:
    grade = "B-"
elif percentage >= 60:
    grade = "C+"
elif percentage >= 55:
    grade = "C"
elif percentage >= 50:
    grade = "C-"
else:
    grade = "F"


print(grade)

#11. Write a program that prints the first `n` natural numbers.

n = int(input("Enter the value of 'n': "))
if n <= 0:
   for i in range(1, n + 1):
        print(i)

else:
    print("this is not natural numbers")
#12. Write a program that calculates the factorial of a number.

n = int(input("Enter a non-negative int: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    factorial = 1
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"The factorial of {n} is {factorial}")


#13. Write a program that generates a Fibonacci sequence of length `n`.
n = int(input("Enter the length of the Fibonacci sequence: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    fibonacci_sequence = [0]
    print(f"The Fibonacci sequence of length 1 is {fibonacci_sequence}")
elif n == 2:
    fibonacci_sequence = [0, 1]
    print(f"The Fibonacci sequence of length 2 is {fibonacci_sequence}")
else:
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)

#14. Write a program that checks if a given number is prime or not.
number=int(input("enter you positive int number"))
if number<2:
    print('this is not prime')
elif number>=2:
    for i in range(2,number-1):
    
        if number%i==0:
            print('not prime')
            break
        else:
            print("prime")
            break
#15. Write a program that prints the multiplication table of a given number.
number=int(input("enter you number"))
for i in range(1,11):
    num=number*i
    print(num)
    i=i+1

#16. Write a program that finds the sum of all even numbers between 1 and `n`.
n=int(input('enter you number'))
sum=0
start=2
while (start<=n):
    sum=sum+start
    start=start+2
print(sum)

#17. Write a program that reverses a given number.
num=input('enter your number')
print(num[-1::-1])

# 18 Write a program that checks if a given string is a palindrome.
num=input('enter your number')
rever=num[-1::-1]
if num==rever:
    print('palindrome')
else:
    print("not")
#19 Write a program that generates a random number and allows the user to guess it.
import random

random = random.randint(1, 100)
guess = int(input("Guess the number (between 1 and 100): "))

if random==guess:
    print("your guess right")
else:
    print(f"sorry random number is {random} ")

#20. Write a program that finds the greatest common divisor (GCD) of two numbers.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is {gcd}.")










