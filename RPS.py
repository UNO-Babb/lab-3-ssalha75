#RPS.py
#Name: Sara Salha
#Date: 2/5/2025
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  play = "Y"
  while play == "Y":
    player = input("Enter choice (R/P/S): ")
    computer = random.choice(["R", "P", "S"])
    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    elif player == "S":
      print("Player chose Scissors")
    else:
      print("Invalid option")
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    elif computer == "S":
      print("Computer chose Scissors")
    if player == computer:
        print("TIE")
        ties = ties + 1
    elif player == "R" and computer == "S":
        print("You win!")
        wins = wins + 1
    elif player == "R" and computer == "P":
        print("You lose.")
        losses = losses + 1
    elif player == "P" and computer == "R":
        print("You win!")
        wins = wins + 1
    elif player == "P" and computer == "S":
        print("You lose.")
        losses = losses + 1
    elif player == "S" and computer == "P":
        print("You win!")
        wins = wins + 1
    elif player == "S" and computer == "R":
        print("You lose.")
        losses = losses + 1
    play = input("Play again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
