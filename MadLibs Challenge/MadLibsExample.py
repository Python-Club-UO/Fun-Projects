# Need to use the input() function to collect some words from the user
# The string in the function will be their prompt for what they need to input into the console
# Store these words in different variables
name = input("Please give me your name ")
adjective = input("Now an adjective ")
pet = input("What is your favourite animal? ")
name2 = input("What is your best friend's name? ")
past_tense = input("Give me a verb in past tense ")
place = input("Give me a place ")

# Now you need to write your story and use .format() and curly brackets to insert the words into your story
# Remember to get creative! This is just an example
# Test out your story a few times. You may have to specify which inputs you expect from your user so everything makes sense.
# For example, instead of just asking for a verb, specify you need a verb in the past-tense!
print("This is the story of {0} and their {1} pet {2}.  One day, {0} and the {2} were walking and they ran into {3} in the street. {3} was strolling along and the police pulled up trying to arrest them.  {0} and {3} {4} away from the cops and ended up hiding in {5}.".format(name,adjective,pet,name2,past_tense,place))

# Your turn! Practice different formats and types of input. What is the craziest story you can create?
