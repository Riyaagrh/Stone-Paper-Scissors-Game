Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Taking input from player

from random import randint
player = input('Rock(R), Paper(P) or Scissors(S) ?')
print(player, 'vs', end= " ")                                                                         # end= " "  ->  tells python to end with a space instead of a new line

# Taking random input from the computer

chosen = randint(1,3)
if chosen == 1:
    computer = 'R'
elif chosen == 2:
    computer = 'P'
else:
    computer = 'S'
print(computer)

# Check who is the winner

if player == computer:
    print("Game DRAW!")
elif player == 'R' and computer == 'S':
    print('Player won the game')
elif player == 'R' and computer == 'P':
    print('Player won the game')
elif player == 'S' and computer == 'P':
    print('Player won the game')
elif player == 'S' and computer == 'R':
    print('Computer won the game')
elif player == 'P' and computer == 'S':
    print('Computer won the game')
elif player == 'P' and computer == 'R':
    print('Computer won the game')
