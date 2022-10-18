#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#print(len(chosen_word))
dog = []
for l in range (0, len(chosen_word)):
  dog.append("_")
  #print(dog[l], end = "")
print("\n")
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
i = 0
for letter in chosen_word:
    if letter == guess:
      #print("Right")
      dog[i] = guess
      #print(dog)
      i += 1
    else:
      #print("Wrong")
      #print(dog)
      i += 1
for l in range (0, len(dog)):
  print(dog[l], end = " ")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.