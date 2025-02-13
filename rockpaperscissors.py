import random


def play():
    user = input("whats your choice? 'p' for paper, 'r' for rock 's' for scissors\n")
    computer = random.choice (['r', 'p', 's'])
    
    if user == computer:                          
        return "its a tie"
    
   
    #r>s, s>p, p>r
    if is_win(user, computer):
       return "you won!"
    if is_win(computer, user):
       return "you lost!"
   
   
def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
        
print(play())