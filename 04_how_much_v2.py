""" Component 2 (How much) v2
use try/accept and pull error message out of the loop"""

error = "please enter a whole number between 1 and 10\n"
valid = False

# keep asking until a valid amount (1-10) is entered
while not valid:
     try:
         # ask for amount
         user_balance = int(input("How much would you like to play with? $"))

         # check if the amount is too high or low
         if 0 < user_balance <= 10:
             print(f"you are playing with ${user_balance}")
             valid = True
         else: print(error)

     except Value_error:
         print(error)
