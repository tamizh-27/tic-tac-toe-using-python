import random as r

# TIC TAC TOE GAME
'''
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

X --> 1 , O --> 0
'''

# Possible win positions
winPos = ['123','456','789','147','258','369','159','357']

# To check win or draw
def check(ttt):
    for win in winPos:
        y = list(win)
        if ttt[int(y[0])-1] == 'X' and ttt[int(y[1])-1] == 'X' and ttt[int(y[2])-1] == 'X':
            print("X wins")
            return 1
        elif ttt[int(y[0])-1] == 'O' and ttt[int(y[1])-1] == 'O' and ttt[int(y[2])-1] == 'O':
            print("O wins")
            return 1
    if ''.join(ttt).isalpha():
        print("Draw Match")
        return 1

# Positions
ttt = [str(i) for i in range(1,10)]

# To print the game
def prin(ttt):
    c = 1
    for i in range(len(ttt)):
        if c % 3 == 0:
            if i == 8:
                print(" " + ttt[i])
            else:
                print(" " + ttt[i])
                print("---|---|---")
                c = 1
        else:
            print(" " + ttt[i] + " |",end="")
            c += 1


# Beginner Level AI
def begAI(ttt,user,bot):
    for ai_win in winPos:
        y = list(ai_win)
        # For AI to win
        if ttt[int(y[0])-1].isnumeric() and ttt[int(y[1])-1] == bot and ttt[int(y[2])-1] == bot:
            return int(y[0])
        if ttt[int(y[0])-1] == bot and ttt[int(y[1])-1].isnumeric() and ttt[int(y[2])-1] == bot:
            return int(y[1])
        if ttt[int(y[0])-1] == bot and ttt[int(y[1])-1] == bot and ttt[int(y[2])-1].isnumeric():
            return int(y[2])
    for ai_win in winPos:
        y = list(ai_win)
        # For AI to block user's move
        if ttt[int(y[0])-1].isnumeric() and ttt[int(y[1])-1] == user and ttt[int(y[2])-1] == user:
            return int(y[0])
        if ttt[int(y[0])-1] == user and ttt[int(y[1])-1].isnumeric() and ttt[int(y[2])-1] == user:
            return int(y[1])
        if ttt[int(y[0])-1] == user and ttt[int(y[1])-1] == user and ttt[int(y[2])-1].isnumeric():
            return int(y[2])
    else:
        return 0
    

print("--- WELCOME TO PY-XO GAME ---")

# Input user to play vs AI (or) Human
inp = input("PvP (or) AI : ")

prin(ttt)

if inp.lower() == "ai":
    x_o = input("Do you want to be X (or) O ? --> ")
    if x_o.lower() == 'x':
        user = "X"
        bot = "O"
    elif x_o.lower() == 'o':
        user = "O"
        bot = "X"

# List for AI 
aixo = ttt.copy()

# The first turn is always X
x = 1

# Main code starts
while True:
    # Player VS Player
    if inp.lower() == "pvp" or inp.lower() == "2p" or inp.lower() == "human":
        n = int(input("Enter the position (1 to 9) : "))

    # Human Vs AI
    elif inp.lower() == "ai":
        
        # If user is X and AI is O
        if user == "X" and bot == "O":
            if x:
                n = int(input("Enter the position (1 to 9) : "))
            else:
                ret = begAI(ttt,user,bot)
                if ret:
                    n = ret
                else:
                    n = int(r.choice(aixo))
                print("AI kept at position ",n)
                
        # If AI is X and user is O
        else:
            if x:
                ret = begAI(ttt,user,bot)
                if ret:
                    n = ret
                else:
                    n = int(r.choice(aixo))
                    print("AI kept at position ",n)
            else:
                n = int(input("Enter the position (1 to 9) : "))                
    
    # To check the number entered between 1 to 9
    if n >= 1 and n <= 9:
        # To check the position is not entered again
        if ttt[n-1].isnumeric():
            if x:
                aixo.remove(str(n))
                ttt[n-1] = 'X'
                x = 0
            else:
                aixo.remove(str(n))
                ttt[n-1] = 'O'
                x = 1
            prin(ttt)
            if check(ttt):
                break
            if x:
                print("\t\t--- X's turn ---")
                print()
                x = 1
            else:
                print("\t\t--- O's turn ---")
                print()
                x = 0
        else:
            print("Position entered already")
    else:
        print("Invalid Position")
        
"""

class Game:
    def __init__(self):
        self.winPos = ['123','456','789','147','258','369','159','357']         # Possible win positions
        self.ttt = [str(i) for i in range(1,10)]                                # Positions
        self.x = 1                                                              # X --> 1 , O --> 0


    # To check win or draw
    def check(self,ttt):
        for win in self.winPos:
            y = list(win)
            if self.ttt[int(y[0])-1] == 'X' and self.ttt[int(y[1])-1] == 'X' and self.ttt[int(y[2])-1] == 'X':
                print("X wins")
                return 1
            elif self.ttt[int(y[0])-1] == 'O' and self.ttt[int(y[1])-1] == 'O' and self.ttt[int(y[2])-1] == 'O':
                print("O wins")
                return 1
        if ''.join(self.ttt).isalpha():
            print("Draw Match")
            return 1

    # To print the game
    def prin(self,ttt):
        c = 1
        for i in range(len(self.ttt)):
            if c % 3 == 0:
                if i == 8:
                    print(" " + self.ttt[i])
                else:
                    print(" " + self.ttt[i])
                    print("---|---|---")
                    c = 1
            else:
                print(" " + self.ttt[i] + " |",end="")
                c += 1
                
    # Main code starts
    def start(self):
        self.prin(self.ttt)
        while True:
            n = int(input("Enter the position (1 to 9) : "))
            if n >= 1 and n <= 9:                                       # To check the number entered between 1 to 9
                if self.ttt[n-1].isnumeric():                                # To check the position is not entered again
                    if self.x:
                        self.ttt[n-1] = 'X'
                        self.x = 0
                    else:
                        self.ttt[n-1] = 'O'
                        self.x = 1
                    self.prin(self.ttt)
                    if self.check(self.ttt):
                        break
                    if self.x:
                        print("\t\t--- X's turn ---")
                        print()
                        self.x = 1
                    else:
                        print("\t\t--- O's turn ---")
                        print()
                        self.x = 0
                else:
                    print("\nPosition entered already\n")
            else:
                print("\nInvalid Position\n")

gam = Game()
gam.start()
"""
