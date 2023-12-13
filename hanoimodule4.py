# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:48:10 2023

@author: iliat
"""

from simpleai.search import SearchProblem, astar

class TowersOfHanoi(SearchProblem):
    def __init__(self, num_disks):
        super().__init__(initial_state=((), tuple(range(num_disks)), ()))
        self.num_disks = num_disks

    def actions(self, state):
        possible_moves = []
        for source, target in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
            if state[source]:
                if not state[target] or state[target][-1] > state[source][-1]:
                    possible_moves.append((source, target))
        return possible_moves

    def result(self, state, action):
        source, target = action
        disk = state[source][-1]
        new_source = state[source][:-1]
        new_target = state[target] + (disk,)
        new_state = list(state[:])
        new_state[source] = tuple(new_source)
        new_state[target] = tuple(new_target)
        return tuple(new_state)

    def is_goal(self, state):
        return state == ((0,), (1,), (2,) + tuple(range(self.num_disks - 1)))

    def heuristic(self, state):
        return sum(len(state[i]) for i in range(3))

problem = TowersOfHanoi(num_disks=3)
result = astar(problem)

actions = [action[1] for action in result.path()]

print("Actions to solve the Towers of Hanoi:")
print(actions)
