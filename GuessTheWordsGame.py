import random

hang_man_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


lists=["sneha","raj","kumar"]

lives = 6
choice = random.choice(lists)
print(choice)   # (you may remove this, it shows the answer)
word_length = len(choice)

game_over = False
correct_letters = []

# create initial display
display = "_" * word_length
print(display)

while not game_over:
    guess = input("choose a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed that letter.")
        continue

    correct_letters.append(guess)

    # update display
    display = ""
    for position in range(word_length):
        if choice[position] in correct_letters:
            display += choice[position]
        else:
            display += "_"
    print(display)

    # wrong guess
    if guess not in choice:
        lives -= 1
        print(hang_man_stages[lives])
        if lives == 0:
            game_over = True
            print("You lose.")

    # check win
    if "_" not in display:
        game_over = True
        print("You win!")
