#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:47 2018

@author: iswariya
"""

import sys
import timeit
import logging
from helper import *


def astar_search(puzzle, opt):
    """Function to implement the A-star search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : [type]
        [description]
    opt : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    prio_list = []
    g_score = 0  # cost function value
    h_score = get_h_score(opt, puzzle.initial_state)  # heuristic function value
    f_score = g_score + h_score  # evaluation function value

    # Creating a heap from list to store the nodes with the priority h_score
    heappush(prio_list, (f_score, puzzle.initial_state))

    explored = []
    step_ctr = 0

    while prio_list:
        step_ctr += 1

        # Get element from prio_queue and add to set of explored nodes
        current_prio_tuple = heappop(prio_list)
        current_state = current_prio_tuple[1]
        explored.append(current_state)

        # Check for goal state
        if current_state == puzzle.goal_state:
            break

        # Check all possible moves and push to prio-queue if not already in there
        possible_actions = get_possible_moves(current_state)
        for child_node in possible_actions:
            if (child_node not in prio_list) and (child_node not in explored):
                f_score = get_h_score(opt, child_node) + step_ctr
                heappush(prio_list, (f_score, child_node))

    final_path = filter_unvalid_moves(explored)
    final_path.append(puzzle.goal_state)

    return final_path


if __name__ == '__main__':
    # Declarations for example initial states
    # tile_list = [1, 0, 2, 3, 4, 5, 6, 7, 8] # Very easy configuration for testing
    tile_list = [0, 1, 2, 3, 4, 5, 8, 6, 7]  # First configuration for testing
    # tile_list = [8, 7, 6, 5, 1, 4, 2, 0, 3]  # Second configuration for testing
    # tile_list = [1, 5, 7, 3, 6, 2, 0, 4, 8]  # Final configuration for testing

    # tile_list = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Very easy 15-puzzle configuration for testing
    # tile_list = [5, 8, 15, 3, 12, 2, 10, 0, 11, 13, 4, 6, 1, 14, 9, 7]  # Final 15-puzzle configuration for testing

    puzzle = Puzzle(tile_list)

    # Get cli argument for the desired heuristic
    opt = int(sys.argv[1])

    # Set logging settings
    logging.basicConfig(
        filename='../results/astar-search-{}-puzzle-{}.log.txt'.format(len(tile_list) -1 , opt),
        filemode='w',
        format='%(message)s',
        level=logging.INFO)

    logging.info("Initial Configuration:" + print_puzzle(tile_list))

    if opt not in [1, 2]:
        logging.info("{} is an invalid heuristic choice".format(opt))
        exit()

    if opt == 1:
        logging.info("Starting A-star with Manhattan Distance heuristic.")
    elif opt == 2:
        logging.info("Starting A-star with Misplaced Tiles heuristic.")

    start_time = timeit.default_timer()
    solution = astar_search(puzzle, opt)
    end_time = timeit.default_timer()
    logging.info('Done! Time taken: {}s'.format(end_time - start_time))

    logging.info("{} moves required:".format(len(solution)))
    for move in solution:
        logging.info(print_puzzle(move))

