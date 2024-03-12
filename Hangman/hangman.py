import random
from words import word_list

class Hangman():
    def __init__(self):
        self.words = word_list

    def randWord(self):
        return random.choice(self.words)

    def blanks(self, rand_word):
        return "_" * len(rand_word)

    def player_input(self):
        return input("Guess the letter or word: ").lower()

    def put(self, player_guess, rand_word, blanks):
        if player_guess == rand_word:
            return True
        for i in range(len(rand_word)):
            if player_guess == rand_word[i]:
                blanks = blanks[:i] + player_guess + blanks[i+1:]
        print(blanks)
        return "_" not in blanks

    def check(self, player_guess, rand_word, tries, win):
        if player_guess not in rand_word:
            tries -= 1
            print(self.display_hangman(tries))
        if tries == 0:
            win = False
        return win, tries

    def display_hangman(self, tries):
        stages = [  # final state: head, torso, both arms, and both legs
            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,
            # head, torso, both arms, and one leg
            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                    """,
            # head, torso, and both arms
            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                    """,
            # head, torso, and one arm
            """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                    """,
            # head and torso
            """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    """,
            # head
            """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    """,
            # initial empty state
            """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    """,
        ]
        return stages[tries]

def game():
    hangman = Hangman()
    tries = 7
    win = False
    rand_word = hangman.randWord()
    print("Random word (displayed for debugging):", rand_word)
    blanks = hangman.blanks(rand_word)

    print("Welcome to Hangman Game!\nLet's play\n")
    print(blanks)

    while tries > 0:
        player_guess = hangman.player_input()
        win = hangman.put(player_guess, rand_word, blanks)
        win, tries = hangman.check(player_guess, rand_word, tries, win)
        if win:
            break




    if win: print("Congrats, you won the game")
    else: print("Don't worry, you will win next time") 
    if input("Do you wanna play one more time? (y/n): ").lower() != "y": print("Thank you for playing!")
    else: game()
        


if __name__ == "__main__":
    game()