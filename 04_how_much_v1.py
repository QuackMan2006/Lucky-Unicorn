""" Component (How much) v1
Ask user how much they want to play with and check that the input is a valid
integer between 1-10. if it is, thi amount becomes the balance in their
 account"""


user_balance = int(input("How much do you want to play with? (must be an "
                         "integer between 1 and 10 $"))


# keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10")
    # ask fo the input
    user_balance = int(input("How much do you want to play with? $"))

print(f"you are playing with ${user_balance}")
