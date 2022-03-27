# Common Tricks
## Bit tricks

- Get least significant 1-bit
  - `x & (-x)`
- Get sum from AND and OR
  - `a + b = (a & b) + (a | b)`

## Segment
### Find Segment containment
Suppose we have list of segements `[l_i,r_i]`. To find containment, i.e. `l_i <= l_j <= r_j <= r_i`, we iterate in decreasing order of `l_i` and find the `r_j` that are less than or equal to the current `r_i`. We can use a Fenwick Tree to count the number of containing segments faster.

## Tree
### Classifying nodes
It is often useful to classify nodes with some recursive relation. 
- In 1566E, we can classify all nodes into "leaves" and "buds" (internal node with only leaf children). Not all "leaves" are actual leaves, but they become leaves after lower buds are lifted. Same with "buds"

## Primes
### Prime divisor count
The amount of distinct sets of prime divisors which the product does not exceed C for such constraints does not exceed `ceil(0.65 * C)`.

## Small constants
### Pairs
See if there is something that you can find out about all the pairs/triples/etc. that helps the whole problem. 