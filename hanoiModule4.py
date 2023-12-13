"""
Created on Tue Dec  5 22:54:11 2023
This is a Towers of Hanoi with 3 disks example. To keep the flow of the 
program, commentary follows at the end.

@author: iliat
"""

from simpleai.search import SearchProblem, astar

class TowersOfHanoi(SearchProblem):
    def __init__(self, num_disks):
        super().__init__(initial_state=((), tuple(range(num_disks)), ()))
        self.num_disks = num_disks

    def actions(self, state):
        actions = []
        for i in range(3):
            if state[i]:
                for j in range(3):
                    if i != j and (not state[j] or state[j][-1] > state[i][-1]):
                        actions.append((i, j))
        return actions

    def result(self, state, action):
        source, target = action
        disk = state[source][-1]
        new_state = list(state)
        new_state[source] = tuple(d for d in state[source][:-1])
        new_state[target] = tuple(d for d in state[target]) + (disk,)
        return tuple(new_state)

    def is_goal(self, state):
        return len(state[0]) == 0 and len(state[1]) == 0

    def heuristic(self, state):
        return len(state[0]) + len(state[1])

# Solve the Towers of Hanoi problem for 3 disks
problem = TowersOfHanoi(num_disks=3)
result = astar(problem)

print("Actions to solve the Towers of Hanoi:")
if result:
    for action in result.path():
        print(action)
else:
    print("No solution found.")
    
'''
The program above uses the A* search algorithm. This is evident from the line:
result = astar(problem)
The astar function from the simpleai.search module implements the A* search 
algorithm to find the solution to the defined problem (TowersOfHanoi in this 
case). A* search combines the advantages of both uniform-cost search and 
greedy search by using a heuristic function to guide the search while 
ensuring optimality (if the heuristic is admissible and the problem is 
defined properly).

A* search is complete if a solution exists and if the heuristic function used 
is both admissible and consistent. In the case of the Towers of Hanoi problem,
the A* search algorithm is complete because it will eventually find a solution
if one exists.

The admissibility of A* search relies on the heuristic function used. An 
admissible heuristic never overestimates the cost of reaching the goal from 
any given state. The heuristic used in this implementation computes the sum 
of the disks that have not reached their destination yet and the number of 
moves required to place the largest disk on the destination peg. This 
heuristic is admissible because it underestimates the number of moves 
required to reach the goal state.

A* search utilizes an evaluation function that combines the cost to reach a 
state from the initial state (g(n)) and the estimated cost to reach the goal 
from that state (h(n)). The evaluation function used in A* search is 
f(n) = g(n) + h(n).

In terms of space efficiency, A* search may require a large amount of memory 
because it needs to store all generated nodes in memory until a solution is 
found. However, A* can be optimized in terms of memory usage by implementing 
techniques like iterative deepening or using techniques to reduce memory 
overhead.

Advantages of A* search:

Completeness: It is guaranteed to find a solution if one exists.
Optimality: It finds the optimal solution if the heuristic is admissible.
Versatility: A* can be applied to a wide range of problems efficiently.
Disadvantages of A* search:

Memory usage: It can consume a lot of memory, especially in larger search 
spaces.
Heuristic requirement: A* relies on a good heuristic function to be effective.
For the Towers of Hanoi problem or similar problems with well-defined 
heuristics, A* search can be advantageous due to its ability to find optimal 
solutions efficiently. However, in larger search spaces with less defined 
heuristics, A* might face challenges related to memory usage and might not 
be the most efficient algorithm.
'''
