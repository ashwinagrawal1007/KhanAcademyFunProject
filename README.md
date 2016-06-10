## Introduction

This implements infection for releasing features at Khan Academy with a/b testing while cosidering user relationships. The representation of the problem in correct data structure and the algorithm to solve it is really important. Adjacency lists and breadth first traversal were used in this solution. 'Is coached by' and 'coaches' are two different relationships; in the context of the problem it is the same. If two users share any one of these relationships, infecting one would result in infecting the other. Using adjacency list to represent the graph makes it really simple to solve and visualize the problem.

## Tests

```sh
python test.py
```

Test cases are present in the test.py, more test cases can be added to test them against the solution. All the test cases follow the spec to ensure correctness of the solution. There are two disjoint subgraphs in the userbase in the test script.
