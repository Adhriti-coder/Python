import random
print("Rock Paper Scissors!")
while True:
    player_choice = input("What would you pick? Rock, paper or scissors? ").lower()
    rock_paper_scissor = ["rock","paper","scissors"]
    computer_choice = random.choice(rock_paper_scissor)
    print(f"You have selected {player_choice} and the computer has selected {computer_choice}!")
    if player_choice==computer_choice:
        print("*********** Its a tie  ***************")
    else:
        if (player_choice=="rock" and computer_choice=="paper") or (player_choice=="scissor" and computer_choice=="rock"):
            print("Mr computer you turned out to be the winner !!")
        else:
            print("Player wins!")
    print("Do you want to play more (Y/N)?")
    ch=input()
    if ch=="N":
        break
       

