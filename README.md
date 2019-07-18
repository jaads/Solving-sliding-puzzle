# Solving sliding puzzle
This project is about solving a sliding puzzle using _informed (heuristic) search algorithms_.
In fact, the following two algorithms are provided.
* **Greedy best-first search** which tries to expand the node that is closest to the goal on the grounds that this is likely to lead to a solution quickly. 
Thus, it evaluates nodes by using just the
heuristic function; that is, `f(n)=h(n)` [Russell,Norvig]
* **A\* search algorithm**, which evaluates nodes by combining `g(n)`, the cost to reach the node, and `h(n)`, the cost
to get from the node to the goal: `f(n) = g(n) + h(n)`.

Both implementations are based on the _uniform cost search_ pseudo code from [Russell,Norvig] on page 84.

As for the heuristic function two strategies are provided: 
* Manhattan Distance
* Misplaced Tiles 


## How to use
Some example initial board configuration is hard coded in the main function. 
If you would like to find a solution for another initial board configuration, adopted the list there.
Also, the code is developed in a generic matter, which makes it possible not only to solve a 8-puzzle, but also e.g. a 15-puzzle. 

To run the solver use `A_star_search.py` or `Greedy_search.py` with an argument of 1 (for _manhattan distance_) or 2 (for _misplaced tiles_ heuristic).

After executing the results, aka the solution to the puzzle, is stored in the `results` folder. 
The txt file contains the initial board configuration and the final board configuration along with the path to reach the goal and the required time taken by the search algorithms.

## Measuring problem-solving performance
Let _b_ be the branching factor and _d_ the depth and _m_ max. depth.

|Algorithmus|Complete|Optimal|Space and time complexity|
|---:|---|---|---|
|Greedy Search|Yes|No|O(b^m)|O(b^m)|
|A*|Yes|Yes|O(b^d) (worst-case)||

## Fun facts
Possible different states for n-puzzle: `n!/2` which is:

|Number of tiles n|Possible of states|
|---:|---:|
|8|181,440|
|15|1,3 trillion|
|24|10^25|


[Russell,Norvig] = Stuart Russell and Peter Norvig: Artificial Intelligence: A Modern Approach, 2009, 3rd edition, Prentice Hall Press (Upper Saddle River, NJ, USA) ISBN: 0136042597 9780136042594 

