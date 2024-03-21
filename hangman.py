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

word_list = ["mouse","carrot","Keyboard","bottle"]
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



