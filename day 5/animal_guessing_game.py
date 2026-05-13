"""

Input:
A string containing an attribute guess or the guess of the animal's name

process:
- randomly select an animal
- allow the user to guess until they guess the correct animal
- when they guess, tell them if the animal has the attribute or not
- tell the user when they guess correctly

Output:
- attribute guess correctness
- congrats bro message

"""

import random #teach python how to do random stuff

#unchanging variables, signal to yourself in caps
ANIMALS = {
    "Lion" : ["Mammal", "Four legs", "Predator", "Carnivore", "Mane", "Feline", "Claws", "Africa", "Fur"],
    "Hyena" : ["Mammal", "Four legs", "Predator", "Carnivore", "Spots", "Claws", "Africa", "Scavenger", "Fur"],
    "Pigeon" : ["Bird", "Two legs", "Wings", "Omnivore", "Scavenger", "Grey", "Flock", "Feathers"],
    "Cat" : ["Mammal", "Four legs", "Predator", "Carnivore", "Pet", "Feline", "Claws", "Fur"],
    "Human" : ["Mammal", "No claws", "Omnivore", "Predator", "Two legs", "Fur", "All colors", "All over the world"],
    "Goldfish" : ["Aquatic", "Fish", "Fins", "Prey", "Omnivore", "Pet", "No legs", "No claws", "Scales"],
    "Lizard" : ["Reptile", "Four legs", "Prey", "Predator", "Carnivore", "Pet", "Claws", "Scales"],
    "Panther" : ["Mammal", "Claws", "Black", "Spots", "Predator", "Jungle", "Carnivore", "Four legs", "Fur"],
    "Eagle" : ["Bird", "Two legs", "Wings", "Predator", "Carnivore", "Flies", "Claws", "Solitary", "Feathers"]
}

WELCOME_MESSAGE = """Animal guessing game
I have icked a random animal. Guess an
attribute or the name of the animal.
"""

CONGRATS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATS_MESSAGE)
    elif guess == "Exit":
        break
    else:
        print(f"No, {guess} is not an attribute of the animal.")
