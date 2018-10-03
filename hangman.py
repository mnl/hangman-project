#!/usr/bin/env python3
# Mickes hangman game
import random
#to draw in terminal
import shutil
term = shutil.get_terminal_size((80,20))

# Helper functions
def validinput(char):
    if len(char) is 1 and char.isalpha() and char is not "":
        return True
    else: return False

def find(s,ch):
    return (i for i, ltr in enumerate(s) if ltr == ch)

class Player:
    """ This class keeps the player name and score"""
    def __init__(self, name):
        self.name = name.capitalize()
        self.score = 0
        self.highscore = 0

    def setscore(self, score):
        self.score += score
        self.highscore += self.score
    def getscore():
        return self.score

class TerminalTyper:
    """ Prints all the game information in the terminal window"""
    statustext = playertext = ""
    state = 0 #Hangman state
    
    def clear(self):
        # Just fill with newlines so old stuff is pushed off screen
        print("\n"*term.lines)

    def update(self):
        self.centertext = self.centertext.center(term.columns)
        print(" "*term.columns)
        print(" "+self.playertext.ljust(term.columns//2))
        print(self.statustext.rjust(term.columns-1))
        print("_"*term.columns)
        print("\n"*8)
        self.hangman()
        print("\n",self.centertext)
        print("\n"*(term.lines-29))

        #setters for game data
    def setcenter(self,data):
        self.centertext = str(data)
    def setstatus(self,string):
        self.statustext = string
    def setplayertext(self,string):
        self.playertext = string
    def input(self,prompt):
        self.update()
        return input(prompt)
    
        # Prints a list as a centered text block
    def textblock(self,text):
        self.hangman()
        p = " "*((term.columns//2)-16)
        print(f"{p}"+f"\n{p}".join(text).center(term.columns))

    def hangman(self):
        state = self.state

        # pad left side with p to get hangman in the center
        p = " "*((term.columns//2)-8)
        
        # Print different hangman depending on state
        # these are 10 different figures printed during the game
        # Plus start, win and lose scenarios.
        if state == 0:
            print('\n'*1)
            print(f'{p}     N  G  M\n{p}   A'+' '*9+f'A\n{p}H'+" "*15+'N')
            print('\n'*5)
        elif state == 1:
            print('\n'*9+p+' _______________\n'+p+'/               \\')
        elif state == 2:
            print(('\n'+f'{p} ||\n'*8)+p+' ||'+'_'*13+p+f'\n{p}/'+' '*15+'\\')
        elif state == 3:
            print(f'{p} ['+'='*8+']\n'+(f'{p} ||\n'*8)+p+' ||'+'_'*13+f'\n{p}/'+' '*15+'\\')
        elif state == 4:
            print(f'{p} ['+'='*8+']\n'+(f'{p} ||\n'*6)+f'{p} | \\\n{p} ||\\\\\n{p}'+' ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 5:
            # Head
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    ( o o )\n{p} ||     \_^_/')
            print(f'{p} ||\n'*2+f'{p} | \\\n{p} ||\\\\\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 6:
            # Torso
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    '+'{ O o }'+f'\n{p} ||     \_^_/')
            print(f'{p} ||      |  |\n{p} ||      |__|\n{p}'+' | \\')
            print(f'{p} ||\\\\\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 7:
            # One arm
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    '+'{ o o }'+f'\n{p} ||     \_^_/')
            print(f'{p} ||     /|  |\n{p} ||    //|__|\n{p} | \\   "')
            print(f'{p} ||\\\\\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 8:
            # Both arms
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    ( o o )\n{p} ||     \_^_/')
            print(f'{p} ||     /|  |\\\n{p} ||    //|__|\\\\\n{p} | \\   "      "')
            print(f'{p} ||\\\\\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 9:
            # One leg
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    ( o o )\n{p} ||     \_^_/')
            print(f'{p} ||     /|  |\\\n{p} ||    //|__|\\\\\n{p} | \\   " //   "')
            print(f'{p} ||\\\\  _//\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state == 10:
            #All limps
            print(f'{p} ['+'='*8+']')
            print(f'{p} ||      _|_\n{p} ||     /   \~\n{p} ||    ( o o )\n{p} ||     \_^_/')
            print(f'{p} ||     /|  |\\\n{p} ||    //|__|\\\\\n{p} | \\   " //\\\\ "')
            print(f'{p} ||\\\\  _//  \\\\_\n{p} ||_\\\\'+'_'*10+f'\n{p}/'+' '*15+'\\')
        elif state > 100:
            #Win scenario
            print(f'{p} ['+'='*8+']')
            print(f'''{p} ||       '\n{p} ||      ___\n{p} ||     /   \~\n{p} ||    ( o - )v
{p} ||     \_-_///\n{p} ||     /|  |/\n{p} | \   //|  |\n{p} ||\\\\  " //\\\\ 
{p} || \\\\__//__\\\\__     \n{p}/               \\''')
        else:
            #Lose scenario
            print(f'''
{p} [========]
{p} ||      _|_
{p} ||     /   \~
{p} ||    ( x x )
{p} ||     \_o_/
{p} ||     /|  |\\
{p} ||    //|  |\\\\
{p} | \   " //\\\\ "
{p} ||\\\\  _//  \\\\_     
{p} ||_\\\\__________
{p}/               \\''')
#End of Asciiman

def newGame():

    # Prepare the word
    answer = words.pop()
    answer = answer.strip().upper()
    #answer = "BANANA" # Debug
    
    wrong_guesses = []
    right_guesses = ["_" for letter in answer]
    
    draw.state = 0
    current_player = 0

    while "_" in right_guesses:
        draw.setcenter("   ".join(right_guesses))
        guess = ""

        # Take guesses until game is finished
        draw.setplayertext(f" {players[current_player].name}'s turn!")
        guess = draw.input("Guess a letter: ")
        guess = guess.upper()
        
        while not validinput(guess):
            guess = draw.input("? ")

        if guess in wrong_guesses+right_guesses:
            draw.setstatus(f"Already guessed {guess} :: {', '.join(wrong_guesses)}")

        elif guess in answer:
            players[current_player].setscore(10)
            for i in find(answer,guess):
                    right_guesses[i] = guess
            draw.setstatus(f"{guess} is correct! :: {', '.join(wrong_guesses)}")
            draw.setcenter(right_guesses)
                
        elif guess in alphabet:
            # Guess was wrong
            wrong_guesses.append(guess)
            draw.state += 1
            draw.setstatus(f"Wrong! :: {', '.join(wrong_guesses)}")
            # Next players turn
            current_player += 1
            current_player %= len(players)

        # Too many wrong guesses, end game
        if len(wrong_guesses) > 10:
            break

    # Out of while loop
    if len(wrong_guesses) < 10:
        draw.setstatus(f"{players[current_player].name} wins!")
        players[current_player].setscore(100)
        draw.state = 101
    else: 
        draw.setstatus("You lost!")
        draw.state += 1

    draw.setcenter(f"The word was {answer.capitalize()}!")
    # Display and reset this games scores
    scorecard = ""
    for player in players: 
        scorecard += f"{player.name}: {player.score} "
        player.score = 0
    draw.setplayertext(scorecard)
    draw.setstatus("Play a new word?")
    draw.update()

# Set up game

# Get words for the game
with open("common_words.txt") as f:
    words = f.readlines()
random.shuffle(words)
alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ")


# Initiate View
draw = TerminalTyper()
draw.clear()
# Display intro and game rules
draw.textblock(["Welcome to Micke's Hangman Game","Guess the word and win 100 points",
        "Every correct letter gives you","10 points. In multiplayer mode",
        "your turn ends when you guess","incorrectly. Have fun!",' ',' ',' '])

#Initiate players
try:
    p = int(input("How many players? "))
except:
    p = 1
players = [Player(input("Name: ")) for n in range(p)]

# Main loop
while True:
    newGame()
    if input("Press 'y' to play another round. ") is not 'y':
        break

#Display total scores
scores =[]
for player in players:
    scores.append(f"{player.highscore:06}\t{player.name}")
scores.sort(reverse=True)
draw.clear()
draw.state = 101
draw.hangman()
draw.state = 0
printout = ["-.-.-.->>> Highscores <<<-.-.-.-","="*32]
for row in scores:
    printout.append(row)
    printout.append("-"*32)
draw.textblock(printout)
print()
