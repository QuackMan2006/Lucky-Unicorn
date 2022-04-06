"""LU yes / no
simplifies the input by converting it to lower case. also, accepts 'y' or 'n' as
abbreviations. prints results of user choice as well as input - for testing.
"""

# ask user if they have played before
show_instructions = input("Have you played this game before?: ").lower()

# if they say yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

# if they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions")


# otherwise - show error
else:
    print("Please answer 'yes or 'no'")

print(f"You entered '{show_instructions}'")
