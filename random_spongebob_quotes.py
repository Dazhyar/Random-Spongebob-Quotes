import random

quotes = []

with open("spongebob.txt") as file:
    for i in file:
        quotes.append(i)

print(random.choice(quotes))
