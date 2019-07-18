#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""

import copy
import math
from heapq import *


class Puzzle:
    """ Class for a n-puzzle providing a minimalistic game environment."""

    def __init__(self, init_state):
        """Class Construction for initializing the board.

        Parameters
        ----------
        init_state : list
            Initial position of the board obtained from user
        """

        self.PUZZLE_TYPE = len(init_state) - 1
        self.initial_state = init_state
        self.current_state = init_state
        self.goal_state = [i for i in range(0, self.PUZZLE_TYPE + 1)]
        self.explored_states = []


def get_row_size(board):
    return int(math.sqrt(len(board) + 1))


def print_puzzle(board):
    """Function to print the puzzle to the console.

    Parameters
    ----------
    board : list
        Current puzzle configuration
    """

    row_size = get_row_size(board)
    output = '\n'

    for idx, val in enumerate(board):
        output += " {} ".format(val)
        if idx % row_size == row_size - 1:
            output += "\n"

    return output


def move_left(board):
    """Function to move one position left in puzzle if possible.

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration

    Returns
    -------
    tuple (boolean, puzzle)
        boolean represents the possibility to make the desired move
        and puzzle represents either the new puzzle configuration in case of a boolean value of true,
        otherwise the unchanged parametrized puzzle.
    """
    row_size = get_row_size(board)
    index_of_emtpy_tile = board.index(0)
    emtpy_tile_is_on_rightmost_side = index_of_emtpy_tile % row_size == row_size - 1
    result = copy.deepcopy(board)

    if not emtpy_tile_is_on_rightmost_side:
        right_tile_pos = index_of_emtpy_tile + 1
        right_tile = board[right_tile_pos]
        result[index_of_emtpy_tile] = right_tile
        result[right_tile_pos] = 0
        possible = True
    else:
        possible = False

    return possible, result


def move_right(board):
    """Function to move one position right in puzzle if possible.

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Returns
    -------
    tuple (boolean, puzzle)
        boolean represents the possibility to make the desired move
        and puzzle represents either the new puzzle configuration in case of a boolean value of true,
        otherwise the unchanged parametrized puzzle

    """
    index_of_emtpy_tile = board.index(0)
    emtpy_tile_is_on_leftmost_side = index_of_emtpy_tile % get_row_size(board) == 0
    result = copy.deepcopy(board)

    if not emtpy_tile_is_on_leftmost_side:
        right_tile_pos = index_of_emtpy_tile - 1
        right_tile = board[right_tile_pos]
        result[index_of_emtpy_tile] = right_tile
        result[right_tile_pos] = 0
        possible = True
    else:
        possible = False

    return possible, result


def move_up(board):
    """Function to move one position up in puzzle if possible.

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Returns
    -------
    tuple (boolean, puzzle)
        boolean represents the possibility to make the desired move
        and puzzle represents either the new puzzle configuration in case of a boolean value of true,
        otherwise the unchanged parametrized puzzle.
    """
    index_of_emtpy_tile = board.index(0)
    emtpy_tile_is_on_bottom = index_of_emtpy_tile >= (len(board) - get_row_size(board))
    result = copy.deepcopy(board)

    if not emtpy_tile_is_on_bottom:
        underlying_tile_pos = index_of_emtpy_tile + get_row_size(board)
        underlying_tile = board[underlying_tile_pos]
        result[index_of_emtpy_tile] = underlying_tile
        result[underlying_tile_pos] = 0
        possible = True
    else:
        possible = False

    return possible, result


def move_down(board):
    """Function to move one position down in puzzle if possible.

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Returns
    -------
    tuple (boolean, puzzle)
        boolean represents the possibility to make the desired move
        and puzzle represents either the new puzzle configuration in case of a boolean value of true,
        otherwise the unchanged parametrized puzzle.
    """
    index_of_emtpy_tile = board.index(0)
    emtpy_tile_is_on_top = index_of_emtpy_tile < get_row_size(board)
    result = copy.deepcopy(board)

    if not emtpy_tile_is_on_top:
        above_tile_pos = index_of_emtpy_tile - get_row_size(board)
        underlying_tile = board[above_tile_pos]
        result[index_of_emtpy_tile] = underlying_tile
        result[above_tile_pos] = 0
        possible = True
    else:
        possible = False

    return possible, result


def get_possible_moves(board):
    """Function to check whether a move is possible in left,
    right, up, down direction and store it.

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Return
    ------
    list
        A list with all possible moves
    """

    possible_moves = []

    ret_tuple_left = move_left(board)
    ret_tuple_right = move_right(board)
    ret_tuple_up = move_up(board)
    ret_tuple_down = move_down(board)

    if ret_tuple_left[0]:
        possible_moves.append(ret_tuple_left[1])
    if ret_tuple_right[0]:
        possible_moves.append(ret_tuple_right[1])
    if ret_tuple_up[0]:
        possible_moves.append(ret_tuple_up[1])
    if ret_tuple_down[0]:
        possible_moves.append(ret_tuple_down[1])

    return possible_moves


def get_nr_of_misplaced_tiles(board):
    """Function to get the number of misplaced tiles for a
    particular configuration

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Return
    ------
    int
        The amount of misplaced tiles
    """
    result = 0

    for idx, val in enumerate(board):
        if idx != val:
            result += 1

    return result


def get_misplaced_tile_heuristic(puzzle):
    """Function to implement misplaced tiles heuristic in
    combination with get_no_of_misplaced_tiles() for each of
    the search algorithms

    Parameters
    ----------
    puzzle : puzzle
        The puzzle in a particular configuration

    Return
    ------
    heap
        Heap of possible moves prioritized by heuristic
    """

    possible_moves = get_possible_moves(puzzle)

    # Prioritize each move and save tuples to list
    for move in possible_moves:
        h_score = get_nr_of_misplaced_tiles(move)
        heappush(possible_moves, (h_score, move.current_state))

    return possible_moves


def get_manhattan_distance(node):
    """Function to calculate the manhattan distance for a
    particular configuration

    Parameters
    ----------
    puzzle : puzzle
        The puzzle in a particular configuration

    Return
    ------
    int
        The sum manhattan distances for each tile
    """
    result = 0

    for idx, val in enumerate(node):
        if idx != val:
            result += abs(idx - val)

    return result


def get_manhattan_distance_heuristic(board):
    """Function for manhattan distance heuristic in
    combination with get_manhattan_distance() and get_possible_moves().

    Parameters
    ----------
    board : list
        The board of the puzzle in a particular configuration.

    Return
    ------
    heap
        An prioritize list of all possible moves of the current board configuration.
    """

    possible_moves = get_possible_moves(board)
    prioritized_moves = []

    # Prioritize each move and save tuples to list
    for move in possible_moves:
        nr = get_manhattan_distance(move)
        heappush(prioritized_moves, (nr, move.current_state))

    return prioritized_moves


def get_h_score(opt, state):
    if opt == 1:
        return get_manhattan_distance(state)
    else:
        return get_nr_of_misplaced_tiles(state)


def filter_unvalid_moves(explored_list):
    """Filter unvalid moves by reverse parsing
    the explored set and creating a final path list
    """
    explored_list.reverse()
    idx = 0
    final_path = []

    for loop_idx, node in enumerate(explored_list):

        if loop_idx < idx or idx == len(explored_list) - 1:
            continue

        possible_moves = get_possible_moves(node)
        ahead = 1

        while True:
            next = explored_list[idx + ahead]
            if next in possible_moves:
                final_path.append(next)
                idx += ahead
                break
            else:
                ahead += 1

    final_path.reverse()
    return final_path
