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


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
    "Please enter a number between {} and {}\n".format(low, high)


    # keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            #check within the required range
            if low <= response <= high:
                return response
            else: print(error)

        except ValueError:
            print(error)


# main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

else:
    print("program continues")


# ask the user how much they want to play with
user_balance = num_check("How much would you like to with? $", 1, 10)
print(f"you are playing with ${user_balance}")
