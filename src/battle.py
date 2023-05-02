# importing libraries
import random

# Creating a list of people
people = ["blue", "red", "green"]

# Creating a function
def battle_code_generation(people):
    # Creating empty dictionaries
    food = {}
    water = {}
    shelter = {}

    # Creating for loop for people
    for person in people:
        # Generating random numbers
        food[person] = random.randint(1, 10)
        water[person] = random.randint(1, 10)
        shelter[person] = random.randint(1, 10)

    # Creating a list for winner
    winner = []

    # Creating for loop for people
    for person in people:
        # Comparing numbers
        if food[person] > water[person] and food[person] > shelter[person]:
            winner.append(person)

    # Returning winner
    return winner[0]

# Creating a function
def battle_code_generation(people):
    # Creating empty dictionaries
    food = {}
    water = {}
    shelter = {}

    # Creating for loop for people
    for person in people:
        # Generating random numbers
        food[person] = random.randint(1, 10)
        water[person] = random.randint(1, 10)
        shelter[person] = random.randint(1, 10)

    # Creating a list for winner
    winner = []

    # Creating for loop for people
    for person in people:
        # Comparing numbers
        if food[person] > water[person] and food[person] > shelter[person]:
            winner.append(person)

    # Returning winner
    return winner[0]

# Creating a function
def battle_code_generation(people):
    # Creating empty dictionaries
    food = {}
    water = {}
    shelter = {}

    # Creating for loop for people
    for person in people:
        # Generating random numbers
        food[person] = random.randint(1, 10)
        water[person] = random.randint(1, 10)
        shelter[person] = random.randint(1, 10)

    # Creating a list for winner
    winner = []

    # Creating for loop for people
    for person in people:
        # Comparing numbers
        if food[person] > water[person] and food[person] > shelter[person]:
            winner.append(person)

    # Returning winner
    return winner[0]

# Creating a function
def battle_code_generation(people):
    # Creating empty dictionaries
    food = {}
    water = {}
    shelter = {}

    # Creating for loop for people
    for person in people:
        # Generating random numbers
        food[person] = random.randint(1, 10)
        water[person] = random.randint(1, 10)
        shelter[person] = random.randint(1, 10)

    # Creating a list for winner
    winner = []

    # Creating for loop for people
    for person in people:
        # Comparing numbers
        if food[person] > water[person] and food[person] > shelter[person]:
            winner.append(person)

    # Returning winner
    return winner[0]

# Creating a function
def battle_code_generation(people):
    # Creating empty dictionaries
    food = {}
    water = {}
    shelter = {}

    # Creating for loop for people
    for person in people:
        # Generating random numbers
        food[person] = random.randint(1, 10)
        water[person] = random.randint(1, 10)
        shelter[person] = random.randint(1, 10)

    # Creating a list for winner
    winner = []

    # Creating for loop for people
    for person in people:
        # Comparing numbers
        if food[person] > water[person] and food[person] > shelter[person]:
            winner.append(person)

    # Checking if there is a winner
    if len(winner) == 0:
        return None
    else:
        # Returning winner
        return winner[0]


# Calling the function
winner = battle_code_generation(people)

# Writing the winner to a text file
with open("winner.txt", "w") as f:
    f.write(f"{winner} won!")

# Creating a dictionary for scores
scores = {winner: 0}

# Generating a random number for probability of winning again
probability = random.randint(1, 100)

# Updating the scores
scores[winner] = probability

# Writing scores to a text file
with open("scores.txt", "a") as f:
    f.write(f"{winner}: {probability}\n")

# Updating the scores for each round
for person in people:
    scores[person] = scores.get(person, 0) + probability

# Writing scores to a text file
with open("scores.txt", "a") as f:
    for person in people:
        f.write(f"{person}: {scores[person]}\n")

# Printing the scores
print(scores)
