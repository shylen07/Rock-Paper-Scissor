# rock , paper , scissor
import random

user_score = 0
computer_score = 0
total_round = 0
draw_round = 0
play_again = "Yes"
options = ['rock', 'paper', 'scissor']
emojis = {
  'rock': '✊',
  'paper': '🤚',
  'scissor': '✌️',
  'draw': '😐',
  'win': '🎉',
  'lose': '😢'
}

while play_again.lower() != "no":
  total_round += 1
  computer_input = random.choice(options)
  user_input = input("Enter Your Choice (Rock, Paper, or Scissor): ").lower()

  if user_input not in options:
    print("Invalid input.")
    continue

  print("Your choice:", emojis[user_input], end="       ")
  print("Computer's choice:", emojis[computer_input])

  if user_input == computer_input:
    print("--------------------------------------------")
    print("It's a Draw! ", emojis['draw'])
    draw_round += 1
  elif (user_input == 'rock' and computer_input == 'scissor') or \
       (user_input == 'paper' and computer_input == 'rock') or \
       (user_input == 'scissor' and computer_input == 'paper'):
    print("--------------------------------------------")
    print("You Win! ", emojis['win'])
    user_score += 1
  else:
    print("--------------------------------------------")
    print("Computer Wins! ", emojis['lose'])
    computer_score += 1
  print()
  play_again = input("Want to play again? (Yes or No): ").lower()
if play_again == "no":
  print("Total Round : ", total_round)
  print("Draw Round  : ", draw_round)
  print("Your Score  : ", user_score, end="           ")
  print("Computer Score: ", computer_score)
