import random
from re import S

def play():
    user = input("Please pick 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie"

    elif is_win(user, computer):
        return "You won!!"

    return "You lost!"

def is_win(player, opponent):
    if(player == 'r' and opponent == 'S') or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True
    
print(play())