## Introduction

This a very interesting problem, for releasing features with a/b testing to cosider user relationships. To handle things well the representation of the problem in correct data structure is very important and so is the algorithm to solve it. Adjacency lists and breadth first traversal were used to solve the problem. 'Is coached by' and 'coaches' are two different relationships, but in the context of the problem they both mean same i.e. if two users share any one of these relationships, and you decide to infect one, you need to infect the other user too. So using adjacency list to represent the graph makes it really simple to solve and visualize.

## Installation

No other libraries except standard python libraries are used to build the solution.

## Tests

```sh
python test.py
```

Test cases are present in the test.py, more test cases can be added and can be used to test against the solution. All the test cases follow the spec to ensure correctness of the solution.
