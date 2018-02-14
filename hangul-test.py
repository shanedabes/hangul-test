#!/usr/bin/env python

import kroman
from random import randint
import argparse

# Game object
class Game():
    def __init__(self, rounds):
        self.__rounds = rounds
        self.__score = 0
        self.__chars = [chr(randint(44032, 55203)) for i in range(rounds)]
        self.__parsed = [kroman.parse(i) for i in self.__chars]

    # Print in green for correct answer
    def __print_correct(self, msg):
        print('\033[32m{}\033[0m'.format(msg))

    # Print in red for incorrect answer
    def __print_incorrect(self, msg):
        print('\033[31m{}\033[0m'.format(msg))

    # Ask a question for the current character
    def __ask(self, round, char):
        print('Q{}: What is the name of this character?'.format(round))
        print(char)

    # Check if the given answer is correct
    def __check_answer(self, char, parsed, answer):
        if answer == parsed:
            self.__print_correct('Correct! {} is {}.'.format(char, parsed))
            self.__score += 1
        else:
            self.__print_incorrect('Sorry...{} is {}'.format(char, parsed))

    # Game controller function
    def play(self):
        for r, (char, parsed) in enumerate(zip(self.__chars, self.__parsed), 1):
            self.__ask(r, char)
            answer = input('Your answer: ')
            self.__check_answer(char, parsed, answer)
            print()
        print('You got {}/{} questions right.'.format(self.__score,
                                                      self.__rounds))

def main():
    # Command line argument parser
    parser = argparse.ArgumentParser(description='Hangul study/test app')
    parser.add_argument('-n', dest='rounds', type=int, default=10,
                        help='Number of question rounds')
    args = parser.parse_args()

    # Play a game of given number of rounds (default 10)
    g = Game(args.rounds)
    g.play()

if __name__ == '__main__':
    main()
