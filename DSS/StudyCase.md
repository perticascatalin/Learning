# Decision Support Systems - Business Study Case

We start with 2 basic concepts: decision tree and expected value.

First example

Decision Tree and Expected Value: choosing between 2 businesses (eg. lemon stand vs. candy shop), each has 50% chances of success. The profit is 90/-10 for the lemon stand and 100/-30 for the candy shop. However, their expected values are 40 vs. 35.

Second example

A similar logic can be applied to decision trees with more branches. Such is the case with the example in which the question whether to consolidate old or develop new products is asked (level 1). Then each choice can branch in different types of implementations, each with its probability of success and value of returns (level 2).

Development

Each additional layer adds details which help inform to make a better overall decision. The overall probability of a leaf node (outcome) is computed by multiplying all the probabilities from the root. Probability with priors can be computed by multiplying up to a certain level. Expected value from a given state is obtained by weighted average of its leaf nodes.This is called decision tree analysis.