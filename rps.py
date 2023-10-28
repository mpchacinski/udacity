#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def __init__(self):
        self.current_move = random.choice(moves)

    def move(self):
        return self.current_move

    def learn(self, my_move, their_move):
        self.current_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.current_move = random.choice(moves)

    def move(self):
        return self.current_move

    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.current_move = "paper"
        elif my_move == "paper":
            self.current_move = "scissors"
        elif my_move == "scissors":
            self.current_move = "rock"


class HumanPlayer(Player):

    def move(self):

        user_input = ""
        while user_input not in moves:
            user_input = input("Rock, paper, scissors? > ").lower()
        return user_input


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("***Player 1 Wins***")
            self.score_p1 += 1
        elif beats(move2, move1):
            print("***Player 2 Wins***")
            self.score_p2 += 1
        else:
            print("***TIE***")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        print("Game will finish when one player is ahead by two points!!!\n")

        round_no = 1
        while abs(self.score_p1 - self.score_p2) <= 1:
            print(f"Round {round_no}:")
            self.play_round()
            print(f"Player 1 Score: {self.score_p1}\t"
                  f"Player 2 Score: {self.score_p2}\n")
            round_no += 1
        if self.score_p1 > self.score_p2:
            winner = 1
        else:
            winner = 2
        print(f"Game over! Player {winner} wins!!!")
        self.score_p1 = 0
        self.score_p2 = 0
        self.play_again()

    def play_again(self):

        play_again = ""
        while play_again not in ["y", "n"]:
            play_again = input("Would you like to play again (y/n)").lower()

        if play_again == "y":
            print("\nGreat, let's start again!!\n")
            self.play_game()
        else:
            print("OK... anyways, thanks for playing!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
