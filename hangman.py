'''
Hangman.py
'''

import sys
import random


class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print c,
        print

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        self.wordguess = ['_'] * len(word)
        guesses = 0
        remaing = 10
        user_guess = []
        letters = list(word)
        print self.wordguess
        print ('The length of the word is %s' %len(word))
        while guesses < 10:
            print ('You have %s remaing guess' %remaing)
            ch = raw_input('Enter a guess:').lower()
            if ch in user_guess:
                print 'Already Guessed'
            elif ch.isalpha() and len(ch) == 1:
                user_guess.append(ch)
                print ('You have already guessed %s' %user_guess)
                guesses += 1
                remaing -= 1
            else:
                if len(ch) > 1:
                    print 'please enter a letter not a string'
                else:
                    print "please enter a letter in the alphabet"
            result_list = map(lambda x: True if x==ch in letters else False,letters)
            if True not in result_list:
                print '%s is not in the word' %ch
            else:
                positions = [i for i, x in enumerate(result_list) if x]

                for pos in positions:
                    self.wordguess[pos] = ch
            print self.wordguess
            if '_' not in self.wordguess:
                print 'You win!!'
                break

        if '_' in self.wordguess:
            print 'You lose! The word was: %s ' %word
            answer = raw_input('Do you want to play again? y or n ').lower()
            if answer == 'y':
                game = Hangman()
                game.playgame()





            ### Your code goes here:###


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
