#!python3

# pretty much copied from https://github.com/coreyhermanson/100daysofcode

import random
from janken-classes import Roll, Player


def print_header():
    print('----------------------------------------------')
    print('----------------- JENKIN! --------------------')
    print('----------------------------------------------')
    print()


def build_the_three_rolls():
    paper = Roll('paper')
    rock = Roll('rock')
    scissors = Roll('scissors')
    rolls = [rock, paper, scissors]

    return rolls


def get_players_name():
    name = input('Enter your name: ').capitalize()

    return name


def get_player_roll():
    proll = input('What is your play? [r]ock, [p]aper, [s]cissors ')




def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:

        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll()

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print(f'Player 1 threw {p1_roll} and Player 2 threw {p2_roll}')

        # Calculate winner


        # display winner for this round
        print(f'Player {outcome} wins!')

        count += 1

    # Compute who won


if __name__ == '__main__':
    print_header()


