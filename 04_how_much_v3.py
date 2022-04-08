""" Component 2 (How much) v3
more efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""


# main routine
error = "that is not valid input\n"
user_balance = 0

# keep asking until a valid amount (1-10) is entered
while not 0 < user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("Please enter a whole nuber between 1 and 10"
                                 "\nHow uch would you like to pay? $"))
        print()

    except ValueError:
        print(error)

print(f"you are playing with ${user_balance}")
