# Binary Search

An app to play around with a binary search algorithm. It's implemented in Python and it works inside a terminal/command prompt.

![alt text](img/giph_binary_search.gif)

## Run It:

To run this stupid little program you should open the terminal at the same directory as your binary_search.py program, and then type:

```
python binary_search.py
```

### What is a Binary Search Algorithm?
Binary Search is a search algorithm that finds the position of a target value within a sorted array. The main idea behind binary search is a Divide and Conquer algorithm. Like all divide-and-conquer algos, binary search first divides a large array into 2 smaller subarrays and then recursively (or iteratively) operate the subarrays. Binary search reduces the search space to half at each step by taking the middle value and comparing it to the target value and discarding the left or right subarray depending on the comparison.

![alt text](img/binary_search_concept.gif)

### Time Complexity
```
O(log base 2, of N)
```

### Why is Binary Search useful?

Software development examples:

- Debugging a somewhat linear piece of code. if the code has many steps mostly executed in a sequence and there's a bug, you can isolate the bug by finding the earliest step where the code produces results which are different from the expected ones.
- Cherry picking a bad code change from a release candidate. When pushing a large code release in production one would sometimes find that there's a problem with that binary. If reverting the whole release wasn't an option the release engineer would binary search through the code change ids. He would figure out the earliest code change which creates the bug.
- Figuring out resource requirements for a large system. one could try running load tests on the system and binary search for the minimum amount of CPUs required to handle a predicted load. (this approach is better than random guessing but much worse than doing some analysis of your system and doing some good educated guesses)
- Figuring out how big should your cache size be for a serving system or deciding on the TTL for the cache.


