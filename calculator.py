"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def tokenize():
    while True:
        input_string = raw_input(">>>  ")
        tokens = input_string.split()
        if tokens[0] == "q":
            break
        try:
            if tokens[0] == "+":
                print add(tokens[1:])
            elif tokens[0] == "-":
                print subtract(tokens[1:])
            elif tokens[0] == "*":
                print multiply(tokens[1:])
            elif tokens[0] == "/":
                print divide(tokens[1:])
            elif tokens[0] == "square":
                print square(int(tokens[1]))
            elif tokens[0] == "cube":
                print cube(int(tokens[1]))
            elif tokens[0] == "pow":
                print power(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "mod":
                print mod(int(tokens[1]), int(tokens[2]))
        except:
            print "do not recognize prompt, try again!"
    print "Done calculating"

tokenize()
print "Goodbye!"
