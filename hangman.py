import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
  "Aardvark",
  "Albatross",
  "Alpaca",
  "Antelope",
  "Armadillo",
  "Axolotl",
  "Badger",
  "Bat",
  "Bear",
  "Beaver",
  "Bee",
  "Bison",
  "Boar",
  "Bobcat",
  "Camel",
  "Capybara",
  "Caribou",
  "Cassowary",
  "Cat",
  "Cheetah",
  "Chicken",
  "Chimpanzee",
  "Chinchilla",
  "Cobra",
  "Condor",
  "Cow",
  "Coyote",
  "Crab",
  "Crane",
  "Crocodile",
  "Crow",
  "Deer",
  "Dingo",
  "Dog",
  "Dolphin",
  "Donkey",
  "Dove",
  "Duck",
  "Eagle",
  "Echidna",
  "Elephant",
  "Elk",
  "Emu",
  "Flamingo",
  "Fox",
  "Frog",
  "Giraffe",
  "Gorilla",
  "Grasshopper",
  "Hamster",
  "Hare",
  "Hawk",
  "Hedgehog",
  "Hippopotamus",
  "Horse",
  "Hyena",
  "Iguana",
  "Impala",
  "Jackal",
  "Jaguar",
  "Jellyfish",
  "Kangaroo",
  "Koala",
  "Komodo Dragon",
  "Lion",
  "Lizard",
  "Llama",
  "Lobster",
  "Lynx",
  "Manatee",
  "Mandrill",
  "Marmot",
  "Meerkat",
  "Mink",
  "Mole",
  "Monkey",
  "Moose",
  "Mosquito",
  "Mouse",
  "Narwhal",
  "Nightingale",
  "Octopus",
  "Opossum",
  "Orangutan",
  "Ostrich",
  "Otter",
  "Owl",
  "Panda",
  "Panther",
  "Parrot",
  "Peacock",
  "Pelican",
  "Penguin",
  "Pig",
  "Pigeon",
  "Polar Bear",
  "Porcupine",
  "Prairie Dog",
  "Rabbit",
  "Raccoon",
  "Rat",
  "Rattlesnake",
  "Reindeer",
  "Rhinoceros",
  "Salamander",
  "Salmon",
  "Sea Lion",
  "Sea Otter",
  "Sea Turtle",
  "Shark",
  "Sheep",
  "Shrew",
  "Skunk",
  "Sloth",
  "Snake",
  "Spider",
  "Squid",
  "Squirrel",
  "Starfish",
  "Stingray",
  "Swan",
  "Tapir",
  "Tiger",
  "Toad",
  "Tortoise",
  "Toucan",
  "Turkey",
  "Turtle",
  "Tyrannosaurus Rex",
  "Unicorn (mythical)",
  "Viper",
  "Vulture",
  "Walrus",
  "Warthog",
  "Weasel",
  "Whale",
  "Wolf",
  "Wolverine",
  "Wombat",
  "Zebra"
]  

lower_string = ""
for name in range(0,140) :
    lower_string = word_list[name].lower()
    word_list[name] = lower_string
print(word_list)

chosen_word = random.choice(word_list)  # randomly selecting word from word_list
end_of_game = False
lives = 6

display = []
for i in range(0,len(chosen_word)) :
    display.append("_")
 

print(f"Chossen word is {chosen_word}")
  # taking single latter input from user
# lenght = chosen_word.__len__()  # this will provide the lenght of string

while not end_of_game :
    guess = input("Guess a letter : ").lower()
    for position in range(len(chosen_word)) :
        # print(f"Current position : {position}\nCurrent latter : {chosen_word[position]}\nlatter : {guess}")
        if chosen_word[position] == guess :
            display[position] = chosen_word[position]  # display[postion] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display :
        end_of_game = True
        print("You Win.")
    # print(display)
    print(stages[lives])



