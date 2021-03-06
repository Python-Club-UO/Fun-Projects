# This library allows you to pick a number randomly
import random

# Here is the most basic example possible
# Create a list with six possible numbers in it
dice = [1,2,3,4,5,6]

# Use the random.choice() function to pick from the list and print
roll = random.choice(dice)
print(roll)


# Here is another possible example
# Generate a list using the list() and range() functions
# Remember, the stop argument in range() isn't included so I put a range of 1-7
dice2 = list(range(1,7))

# I used random.choice() again to select a random number
# This time I printed a message. I needed to convert the roll2 variable to a string as well
# I used the str() function to convert it to a string
roll2 = random.choice(dice2)
print("You rolled a " + str(roll2))


# Take a look at the advanced example for some more complex solutions
# Don't forget to test your code to make sure the numbers are generating randomly each time 
