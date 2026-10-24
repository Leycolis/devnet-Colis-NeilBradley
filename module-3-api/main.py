import requests
import random 

p1 = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')
p2 = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
p3 = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle')
p4 = requests.get('https://pokeapi.co/api/v2/pokemon/blastoise')
p5 = requests.get('https://pokeapi.co/api/v2/pokemon/caterpie')

name = p1.json()['name']
height = p1.json()['height']
weight = p1.json()['weight']

name = p2.json()['name']
height = p2.json()['height']
weight = p2.json()['weight']

name = p3.json()['name']
height = p3.json()['height']
weight = p3.json()['weight']

name = p4.json()['name']
height = p4.json()['height']
weight = p4.json()['weight']

name = p5.json()['name']
height = p5.json()['height']
weight = p5.json()['weight']

pokemon_namelist = ["charmander" , "ditto" , "squirtle" , "blastoise" , "caterpie"]
The_name = random.choice(pokemon_namelist)
print(The_name)
