'''2. Create a Python program that calculates and prints the area of a circle. 
Input format  
The first line of each test case consists of an integer as N. 
Output format  
Print the area of a circle. 
Constraints  
The radius should be a positive floating-point number. 
The program assumes that the user will enter a valid radius value. 
The program will calculate and print the area without any specific limitations on the radius 
value as long as it's a valid positive number. 
The program uses an approximate value of π (pi) for the calculation, and this approximation 
may not be as accurate as using the math module.'''
import math

number =float(input("Enter the radious"))
radious=math.pi*(number*number)
print(f"The area of the circle with radius 5.0 is: {radious:5f}")

