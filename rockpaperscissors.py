import random
import re
def play():
    user = input("Enter your choice:\nfor rock: 'r'\nfor paper: 'p'\nfor scissors: 's'\n").lower()
    computer = random.choice(['r','p','s'])
    print(user)
    try:
        valid_input = r"['r','s','p']"
        if re.search(valid_input,user):
            if user == computer:
                return 'It\'s a tieπ€π€'
    
            if is_win(user,computer):
                return 'You won!π₯³π₯³'

            return 'You lost!ππ'
        else :
            raise ValueError()

    except ValueError:
        print('Wrong Inputβββ')
    
def is_win(player,computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play())
