#!python3

from data import us_state_abbrev
from data import states_list


def print_10th(state_list, state_dict, index):
    """
    print out the 10th item in each"""
    states = [sorted(state_dict.keys())[index - 1], state_list[index - 1]]

    return states


def print_45th(state_dict, index):
    """
    Print out the 45th key in the dictionary"""

    return sorted(state_dict.keys())[index - 1]


def print_27th(state_dict, index):
    """
    Print out the 27th value in the dictionary"""

    return sorted(state_dict.values())[index - 1]


if __name__ == "__main__":
    print(f' DICT 10th: {print_10th(states_list, us_state_abbrev, 10)[0]}')
    print(f' LIST 10th: {print_10th(states_list, us_state_abbrev, 10)[1]}')
    print(f' DICT 45th KEY: {print_45th(us_state_abbrev, 45)}')
    print(f' DICT 27th VALUE: {print_27th(us_state_abbrev, 27)}')

    """
    Replace the 15th key in the dictionary with the 28th item in the list"""
    dict_15_key = sorted(us_state_abbrev.keys())[14]
    list_28_item = states_list[27]

    print(us_state_abbrev)
    us_state_abbrev[list_28_item] = us_state_abbrev.pop(dict_15_key)
    print(us_state_abbrev)
    print(us_state_abbrev[list_28_item])
