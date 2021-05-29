# With an empty list and a for loop and then to append to list

squares = []
for i in range(1, 101):
    squares.append(1**2)

print(squares)
# This gives you  a list from 1 to 10000, each number squared

#Now with list comprehension

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# Does the same work as for loop above


# Example2
# x**2 %5 is trhe same as x^2(mod 5)
remainders5 = [x**2 % 5 for x in range(1, 101)]

print(remainders5)

# Gives a list full of 1s, 4s, and 0s

#Quadratic Reciprocity

p_remainders = [x**2 % p for x in range(0, p)]

len(p_remainders) = p + 1 / 2


# To find a movie with a letter g
# First with an empty list and for loop
# movies variable in for loop is a list of movie names
gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)

# Now with list comprehension

gmovies = [title for title in movies if title.startswith('G')]


# List comprehension using tuples
# Finding movies before year 200

pre2k = [title for (title, year) in movies if year < 200]

# Scalar multiplication
# prints every number in list by 4
v = [2, -3, 1]
w = [4 * v for x in v]

# prints out [8, -12, 4]



# Cartesian Product
# If A and B are sets, then the Cartesian product is the set of pairs (a, b) where 'a' is in A and 'b' is in B.

# Example: 
    # A = {1, 3}
    # B = {x, y}
    # A * B = {(1, x), (1, y), (3, x), (3, y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]

# Prints out all possible pairs of both lists, which equals 16 pairs


