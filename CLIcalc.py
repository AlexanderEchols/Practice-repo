#!/usr/bin/python3
# Script: CLI Calculator 
# Author: Alexander Echols.    
# Date of creation: 26 Sep 2023                
# Date of latest revision:      
# Purpose: create a python script that takes user input and performs basic calculation

#main
# first create a function to run the calculations
def calculate():
    try:
        # store the numbers and component we want to use in the equation
        a = float(input("what is the first number you wish to calculate? "))
        cal = input("What is the component? ")
        b = float(input("What is the second number you wish to use? "))
        # evaluate the equation and store it in the variable "result"
        if cal == "+":
            result = a + b
        elif cal == "-":
            result = a - b
        elif cal == "*":
            result = a * b
        elif cal == "/":
            result = a / b
        #print the result of the equation
        print(result)
    # if there are errors we can store them in the "exc" variable
    except Exception as exc:
        # if there is an error we print it
        print("Invalid expression:", exc)
        
calculate()