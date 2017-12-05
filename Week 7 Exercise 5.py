# imports random library
import random
# declaring a variable which is a list of random answers
rand_answer = ['yes', 'no', 'maybe']
# asking the user for their name
name = input('What is your name: ')
percent = random.randint(1, 100)


# defining a function to get the users name
def get_name():
    return name
# defining a function to generate a random answer from the list given, and to return the chosen word


def random_answer():
    random_word = random.choice(rand_answer)
    return random_word


# prints the users name with a hello message.
print("Hello " + get_name())
# creates a while loop for the questions a user enters
while 1:
    question = str.lower(input('Please enter your question: '))
#    print(question.find("windows"))

    if percent <= 85:
        quit()
    elif question == 'goodbye':
        print("goodbye")
        break
    elif question.find("windows") > -1:
        print("Try rebooting your PC")
    elif question.find("apple") > -1:
        print("This call will cost you £100 per minute")
    elif question.find("phone") > -1:
        print("Complete a factory reset of the phone")
    elif question.find("tablet") > -1:
        print("Connect to your computer to sync up")
    elif question.find("smartboard") > -1:
        print("Recalibrate with the given smart pen")
    else:
        print(random_answer())
