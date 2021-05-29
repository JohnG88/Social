# Anonymous functions = Lambda functions

# Write function to compute 3x + 1

def f(x):
    return 3* x + 1

f(2)
# Will give out seven

# To create a lambda expression first write lambda(lambda) followed by inputs(x). Then add an expression that will be the return value(3 * x + 1).

lambda x: 3 * x + 1

# If written like above it will give off <function <lambda> at 0x01D53etc...>

# So give lambda a variable

g = lambda x: 3 * x + 1

g(2)
# Will give out seven

# Example 2
# To get first and last name from a user registration, and turn into a Full Name
# Below is  lambda  that has two inputs fn = first_name and ln = last_name
# fn.strip() removes whitespace in front and back of string from first_name, will also work with ln(last_name)
# .title() gives of first letter is string is capitalized(as you can see the outcome of comment below lambda)
# " ", is a whitespace added between both strings
full_name = lambda fn, ln: fn.strip().title + " " + ln.strip().title()
full_name(" leonhard", "EULER")

# Will give 'Leonhard Euler'


# General way of writing a lambda
# Fist type lambda
# Then type 0 or more inputs
# Then add an expression after : . The expression is the return value
# Can't use lambdas fro multi-line functions
lambda : "What is my purpose?"
lambda x: 3 * x + 1
lambda x, y: (x * y)**0.5 # Geometric Mean
lambda x, y, z: 3/(1/x + 1/y + 1/z) # Harmonic Mean
# lambda x1, x2, xn: <expression>


# lambda functions with no name
# There is a list of sci-fi author names, the variable of list is scifi_authors
# To check the list's built in method type, help(scifi_authors.sort)
# A line pops up, L.sort(key=None, reverse=False)
# This tutorial passes a lambda expression to key
# Below is to access the last name, split string into pieces, whereever the is a space(name.split(" "))
# [-1] access last piece of splits
# .lower converts all letters to lowercase, so it doesn't become case sensitive
scifi_authors = []
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

# When you type scifi_authors it will be in alphabetical order through last name


# Creating functions that make functions
# Using the Quadratic Formula
# f(x) = ax**2 + bx + c

def build_quadratic_function(a, b, c):
    # Returns the function f(x) = ax**2 + bx + c
    return lambda x: a*x**2 + b*x + c

# Applying numbers to function
f = build_quadratic_function(2, 3, -5)

f(0) # -5
f(1) # 0
f(2) # 9

# can also write
build_quadratic_function(3, 0, 1)(2) # 3x^2 + 1 evaluated for x=2

# returns 13