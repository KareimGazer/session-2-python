
# we use loops to loop over the values of our list
# we store each value of our list in a variable and run the code inside the loop
# the variable number will take the value of each item in the list
# for each value in the list assign it to the variable number and run the code
# inside the loop

for number in [1, 2, 3, 4]:
    print(number)

# we can assign the list to a variable
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

# we can use a for loop to help us instruct our turtle to draw a rectangle
# instead of writing code for the four sides of rectangle
import turtle
amy = turtle.Turtle()
for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.left(90)

# we can generate a list of numbers that we can loop over
# the range is a generator that generates lists of numbers for us that we can loop over
for number in range(1, 5): # [1, 2, 3, 4], 5 not included
    print(number)

# we can use a step of two to get a list of all even numbers from 0 to 10
for number in range(0, 11, 2): # [0, 2, 4, 6, 8, 10], 11 not included
    print(number)


# there is a concise syntax for range to do this
# and generate our list which is called a list comprehension

numbers = [number for number in range(0, 11, 2)] # a list of all even numbers from 0 to 10
print(numbers)

# we can also generate a list of all odd numbers from 0 to 10
numbers = [number for number in range(1, 11, 2)] # a list of all odd numbers from 0 to 10
print(numbers)
