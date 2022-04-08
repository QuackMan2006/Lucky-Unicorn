""" LU yes/no
puts code created in v2 into a loop to make testing easier and more
efficient.
"""

show_instructions = ""
while show_instructions != "x":

    # ask user if they've played before
    show_instructions = input("Have you played this game before? : ")

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
