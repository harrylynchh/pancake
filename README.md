# README.md
## Harry Lynch
### 2/28/2025
### Solving the Pancake Problem
---
    1. Search Problem Definition

    2. Possible Cost Function (Backward Cost)

    3. Possible heuristic function (Forward Cost)

    5.
---
# About:

    This program is designed to solve the pancake problem in as few flips as
    possible using two separate search algorithms, **UCS** and **A\***. My forward cost, or heuristic function used in A* is the 'gap heuristic' sourced from the paper linked in the usage section.  My backward cost, or cost function for both algos is merely the number of flips it takes to get to that individual state-- this allows both algorithms to prioritize finding the fewest flip solution.
---
# Usage:

    - To run the program, execute: python main.py
    - Choose an algorithm type (either U for UCS or A for A*)
    - Then provide a space separated array for the starting configuration
        - NOTE: There is no error checking on this currently so invalid configs
                will probably cause errors or infinite loops
        - The user can also input 'N' to have a random sequence of size 10
          created as the original sequence
    - After running the given/generated sequence on the requested algorithm,
      one can re-run the same initial configuration on the other algorithm.
    - The following statistics are provided on each run:
        - Time: Total time taken to find the goal state (properly sorted cakes)
        - Flips: The sequence of flips that result in the goal state (defined
                 as F~n~ by this paper https://ai.dmi.unibas.ch/papers/helmert-socs2010.pdf)
        - States Accessed: Determined by the length of the set of visited nodes
---
# Resources:
    
    - I referenced stack overflow for some of the more novel complexities of 
      python used in this project (tuple unpacking, lambdas, list comprehensions)
    - I used heapq, random, and time from the python stdlib to handle the priority
      queue data structure, shuffle generated initial states, and time the process
      respectively. No external packages are required to run this program.