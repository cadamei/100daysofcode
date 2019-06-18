#!python3

import random


class Player(name):
    def __init__(self, name):
        self.name = name


class Roll(name):
    def __init__(self, name):
        self.name = name

    # Rolls that can be defeated by self

    # Rolls that defeated self

    """
    1. Rock > Scissors
    2. Paper > Rock
    3. Scissors > Paper
    """


def print_header():
    print('----------------------------------------------')
    print('----------------- JENKIN! --------------------')
    print('----------------------------------------------')
    print()


def build_the_three_rolls():
    pass


def get_players_name():
    pass


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

        p2_roll = random.randint(1, 3)
        p1_roll = ('[s]cissors, [p]aper or [r]ock?')

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print(f'Player 1 threw {p1_roll} and Player 2 threw {p2_roll}')
        # display winner for this round
        print(f'Player {outcome} wins!')

        count += 1

    # Compute who won


if __name__ == '__main__':
    main()
