## Decision Support Systems - Business Study Case

### Decision Tree Analysis

We start with 2 basic concepts: decision tree and expected value.

**First example**

Decision Tree and Expected Value: choosing between 2 businesses (eg. lemon stand vs. candy shop), each has 50% chances of success. The profit is 90/-10 for the lemon stand and 100/-30 for the candy shop. However, their expected values are 40 vs. 35. Example from [1].

**Second example**

A similar logic can be applied to decision trees with more branches. Such is the case with the example in which the question whether to consolidate old or develop new products is asked (level 1). Then each choice can branch in different types of implementations, each with its probability of success and value of returns (level 2). Example from [2].

**Development**

Each additional layer adds details which help inform to make a better overall decision. The overall probability of a leaf node (outcome) is computed by multiplying all the probabilities from the root. Probability with priors can be computed by multiplying up to a certain level. Expected value from a given state is obtained by weighted average of its leaf nodes. This is called decision tree analysis.

### Decision Tree in Machine Learning

We develop on more complex concepts: decision tree and attribute split impurity (gini impurity)

**First example**

Decision trees are also great models for machine learning - automated classification or regression. Such an example is the symptom to cause mapping problem. Given a large number of symptoms (chest pain, nausea, etc.) predict whether the patient has a heart disease. Each symptom is looked at as an attibute and we would like to grow a decision tree with the lowermost splits being the most informative.

The notion of how informative an attribute is can be formulated via the gini impurity which is a measure of how impure a set of observations is. That is, if we were to predict a heart disease, how well is it to make the decision solely on whether the patient has chest pains (yes or no).

### References

[1] Decision Tree Tutorial, mbabullshit.com

[2] Example from slides

[3] Thinking: Fast and Slow, Choices
