import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
choice = int(input()) - 1
choice_list = [rock, paper, scissors]
pc_choice = random.randint(0, 2)
print(f'Your choice :\n{choice_list[choice]}')
print(f'PC choice :\n{choice_list[pc_choice]}')

if choice == pc_choice:
  print('Advice')
elif choice==0 and pc_choice==2 or choice==1 and pc_choice==0 or choice==2 and pc_choice==1:
  print('You WIN!!!')
else:
  print('You LOOSE!!!')