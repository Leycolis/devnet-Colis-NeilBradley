
import requests
import random

pokemon_list = ["charmander", "ditto", "squirtle", "blastoise", "caterpie"]

name = random.choice(pokemon_list)

try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    response.raise_for_status()
    data = response.json()

    height = data["height"] / 10
    weight = data["weight"] / 10

    print("Who's That Pokemon?")
    print("Height:", height, "meters")
    print("Weight:", weight, "kg")

    for attempt in range(3):
        guess = input("Guess the Pokemon: ").lower().strip()

        if guess not in pokemon_list:
            print("Pokemon not in the list!")
        elif guess == name:
            print("Correct! You win!")
            break
        else:
            print("Wrong guess!")

    else:
        print("Game over! It was", name.title())

except requests.exceptions.RequestException:
    print("Error connecting to PokeAPI. Check your internet.")

