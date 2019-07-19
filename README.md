# Solving sliding puzzle
This project is an implementation of a **AI agents** which solve a sliding puzzle using _informed (heuristic) search algorithms_.
In fact, the agents are provided with the following two algorithms.
* **Greedy best-first search** which tries to expand the node that is closest to the goal on the grounds that this is likely to lead to a solution quickly. 
Thus, it evaluates nodes by using just the heuristic function; that is, `f(n)=h(n)` [Russell,Norvig]. This agent can be considered as a **goal-based** agent.
* **A\* search algorithm**, which evaluates nodes by combining `g(n)`, the cost to reach the node, and `h(n)`, the cost
to get from the node to the goal: `f(n) = g(n) + h(n)` [Russell,Norvig]. Therefore `f(n)` describes the estimated cost of the _cheapest_ solution through `n`. 
Thus, this agent can be considered as a **utility-based** agent.

Both implementations are based on the _uniform cost search_ pseudo code from [Russell,Norvig] on page 84.

As for the heuristic function two strategies are provided: 
* **Manhattan Distance**
* **Misplaced Tiles**

## Problem specification
From [Russell,Norvig]: The 8-puzzle for example consists of a 3×3 board with eight numbered tiles and a blank space. 
A tile adjacent to the blank space can slide into the space.
The object is to reach a specified goal state which represent a ordered list of numbers.

- **States**: A state description specifies the location of each of the eight tiles and the blank
in one of the nine squares.
- **Initial state**: Any state can be designated as the initial state. Note that any given goal
can be reached from exactly half of the possible initial states.
- **Actions**: The simplest formulation defines the actions as movements of the blank space
Left, Right, Up, or Down. Different subsets of these are possible depending on where the blank is.
- **Transition model**: Given a state and action, this returns the resulting state; for example,
if we apply Left to the start state in Figure 3.4, the resulting state has the 5 and the blank switched.
- **Goal test**: This checks whether the state matches the goal configuration (Other goal configurations are possible.)
- **Path cost**: Each step costs 1, so the path cost is the number of steps in the path.

## Task environment 
### Specification - PEAS description
|Performance Measure| Environment| Actuators| Sensors| 
|---|---|---|---|
|Number of moves|Puzzle board with n tiles|Computer|Computer|

### Properties
- Fully observable
- Single agent
- Deterministic
- Sequential
- Static
- Discrete
- Known

## Measuring algorithm performance
Let _b_ be the branching factor and _d_ the depth and _m_ max. depth.

|Algorithmus|Complete|Optimal|Space and time complexity|
|---:|---|---|---|
|Greedy Search|Yes|No|O(b^m)|O(b^m)|
|A*|Yes|Yes|O(b^d) (worst-case)||

# How to use
Some example initial board configuration is hard coded in the main function. 
If you would like to find a solution for another initial board configuration, adopted the list there.
Also, the code is developed in a generic matter, which makes it possible not only to solve a 8-puzzle, but also e.g. a 15-puzzle. 

To run the solver use `A_star_search.py` or `Greedy_search.py` with an argument of 1 (for _manhattan distance_) or 2 (for _misplaced tiles_ heuristic).

After executing the results, aka the solution to the puzzle, is stored in the `results` folder. 
The txt file contains the initial board configuration and the final board configuration along with the path to reach the goal and the required time taken by the search algorithms.

# Fun facts
Possible different states for n-puzzle: `n!/2` which is:

|Number of tiles n|Possible of states|
|---:|---:|
|8 (3x3)|181,440|
|15 (4x4)|1,3 trillion|
|24 (5x5)|10^25|


[Russell,Norvig]: Stuart Russell and Peter Norvig: Artificial Intelligence: A Modern Approach, 2009, 3rd edition, Prentice Hall Press (Upper Saddle River, NJ, USA) ISBN: 0136042597 9780136042594 

