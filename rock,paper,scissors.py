import random

print("Welcome to the rock, paper and scissors game.\n All the best!")
player_choice = int(input("Type '0' for rock, '1' for paper and '2' for scissors "))
print("you chose:\n")
if player_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif player_choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif player_choice == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("enter a valid choice")

print("computer chose:\n")
choice = random.randint(0,2)

if choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if player_choice == 0 and choice == 2:
    print("you win!")
elif player_choice == 1 and choice == 0:
    print("you win!")
elif player_choice == 2 and choice == 1:
    print("you win!")
elif player_choice == choice:
    print("it's a draw!")
elif player_choice < choice:
    print("computer wins!")
elif player_choice == 2  and choice == 0:
    print("computer wins!")
else:
    print("play again!")