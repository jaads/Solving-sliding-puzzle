#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jan Arends
"""

import sys
import timeit
import logging
from helper import *


def greedy_search(puzzle, opt):
    """Greedy search algorithm implementation.

    Parameters
    ----------
    puzzle : puzzle
        puzzle with an initial board configuration which must be solved.
    opt : int
        CLI argument which specifies the heuristic function to use.

    Returns
    -------
    list
        A list of all board configurations from the initial state to the goal state.
    """

    # Creating priority queue which holds tuples of the
    # priority value and the corresponding state
    prio__queue = []
    h_score = get_h_score(opt, puzzle.initial_state)
    heappush(prio__queue, (h_score, puzzle.initial_state))

    explored = []
    step_ctr = 0

    while prio__queue:
        step_ctr += 1

        # Get element from prio_queue and add to set of explored nodes
        current_prio_tuple = heappop(prio__queue)
        current_state = current_prio_tuple[1]
        explored.append(current_state)

        # Check for goal state
        if current_state == puzzle.goal_state:
            break

        # Check all possible moves and push to prio-queue if not already in there
        possible_actions = get_possible_moves(current_state)
        for child_node in possible_actions:
            if (child_node not in prio__queue) and (child_node not in explored):
                heappush(prio__queue, (get_h_score(opt, child_node), child_node))

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
        filename='./results/greedy-search-{}-puzzle-{}.log.txt'.format(len(tile_list) - 1, opt),
        filemode='w',
        format='%(message)s',
        level=logging.INFO)

    logging.info("Initial Configuration:" + print_puzzle(tile_list))

    if opt not in [1, 2]:
        logging.info("{} is an invalid heuristic choice".format(opt))
        exit()

    if opt == 1:
        logging.info("Starting Greedy search with Manhattan Distance heuristic.")
    elif opt == 2:
        logging.info("Starting Greedy search with Misplaced Tiles heuristic.")

    start_time = timeit.default_timer()
    solution = greedy_search(puzzle, opt)
    end_time = timeit.default_timer()
    logging.info('Done! Time taken: {}s'.format(end_time - start_time))

    logging.info("{} moves required:".format(len(solution)))
    for move in solution:
        logging.info(print_puzzle(move))
