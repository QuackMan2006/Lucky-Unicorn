""" Component 3 random tokens v1
Generates random choice of tokens in random order"""


import random

tokens = ["unicorn", "horse", "zebra", "donkey"]


# testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # can wrap output making it easier to screenshot

