## Decision Support Systems - Business Study Case

Abstract: exemplify concepts to be applied to a warehouse which intends to increase a set of KPIs. Develop abstractions and visualizations for these KPIs.

### Decision Tree Analysis

We start with 2 basic concepts: decision tree and expected value and provide some realistic examples of their manifestation in practice. Then we emphasize how decision tree analysis relates to empirical evidence for behavioral econimics principles (rational vs. aversity bias).

**First example**

Decision Tree and Expected Value: choosing between 2 businesses (eg. lemon stand vs. candy shop), each has 50% chances of success. The profit is 90/-10 for the lemon stand and 100/-30 for the candy shop. However, their expected values are 40 vs. 35. Example from [1].

**Second example**

A similar logic can be applied to decision trees with more branches. Such is the case with the example in which the question whether to consolidate old or develop new products is asked (level 1) [3]. Then each choice can branch in different types of implementations, each with its probability of success and value of returns (level 2).

**Development**

Each additional layer adds details which help inform to make a better overall decision. The overall probability of a leaf node (outcome) is computed by multiplying all the probabilities from the root. Probability with priors can be computed by multiplying up to a certain level. Expected value from a given state is obtained by weighted average of its leaf nodes. This is called decision tree analysis.

**Behavioral Economics**

Decision tree analysis is a model for making a rational decision in a given context. However, overall human decision making differs [5] and economists have had great challenges in explaining why economics does not work according to theories based on rational behavior. For instance, in [4] we can find examples and a summary of a theory which states that humans do not make decisions based on things like expected value, but instead weigh a lot more losses than gains. That is, the loss L (-5 dollars) vs. the gain (+5 dollars) G has a higher negative impact |L| > |G| than it has a positive impact, under the same probability (0.5). So in this case, an average decision maker would not see it as a neutral decision, but a bad one instead.

|Example from [1] | Example from [2] |
|:-:|:-:|
| ![Decision Tree Analysis](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DSS/decision_tree_1.png)|![Decision ML](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DSS/decision_tree_2.png)|

### Decision Tree in Machine Learning

We develop on more complex concepts: decision tree and attribute split impurity (gini impurity).

**First example**

Decision trees are also great models for machine learning - automated classification or regression. Such an example is the symptom to cause mapping problem. Given a large number of symptoms (chest pain, nausea, etc.) predict whether the patient has a heart disease [2]. Each symptom is looked at as an attibute and we would like to grow a decision tree with the lowermost splits being the most informative.

**Gini Index**

The notion of how informative an attribute is can be formulated via the gini impurity which is a measure of how impure a set of observations is. That is, if we were to predict a heart disease, how well is it to make the decision solely on whether the patient has chest pains (yes Y or no N). G = 1 - Y^2 - N^2.

### Warehouse KPIs

The warehouse we deal with in this study case is an automobile parts importer and distributer which would like to start getting rid of some legacy stocks. These stocks have accumulated for a number of reasons such as market competition changes and bad prediction of demand. We will identify these items through the KPI called velocity (V). The other two KPIs of interest are seed/investment (S) and profit (P). We unify theses KPIs under a model called SPV. 

This model will help us analyze the incentives of the company owning the warehouse, its clients and mixed orders which should be aggregated such that the company makes a trade-off between increasing the velocity of legacy items (the concept of sales) and keeping a satisfactory profit overall.

**SPV Model** (KPIs & levels)

- Seed (investment)
- Profit
- Velocity
- Product level
- Aggregate level (mixed orders)
- Sub-business level
- Business level

**Velocity**

- Identify slow items
- Design measures for slow items
- Analyze slow items/time frame
- Identify product periodicity

**Company incentives**

- Max Profit, Max Velocity

**Client incentives**

- Max Profit, Min Investment

**Objectives**

Use computational tools to monitor KPIs, analyze different levels of the model and predict through decision tree analysis and economic principles which sub-businesses should be followed-through such that the overall business velocity increases at a minimal loss of profit.

### References

[1] Decision Tree Tutorial, mbabullshit.com

[2] StatQuest: Decision Tree

[3] Example from slides

[4] *Thinking: Fast and Slow, Choices*, Daniel Kahneman

[5] *System 1 and System 2 cognition in the decision to adopt and use a new technology*, Vijay Khatri et al