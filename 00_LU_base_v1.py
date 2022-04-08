"""LU base component
components added after they have been created and tested"""


# functions go here...
def yes_no(question_text):
    while True:

        # ask user if they've played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise - show error
        else:
            print("Please answer 'yes or 'no'")


# function to display instructions
def instructions():
    print("**** How to play *****")
    print()
    print("the rules of the game will go here")
    print()
    print("program continues")
    print()


# main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

else:
    print("program continues")
