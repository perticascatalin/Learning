# Constraint Programming in Genetic Algorithms: Report

### Abstract

This study presents the initial ideas gathered while trying to model the processes involved in genetic algorithms as constraint satisfaction problems (and constraint optimization). We present 2 ideas: pairing and resemblance, which try to formalize the selection and the crossover steps from evolutionary algorithms into constraint satisfaction problems. To do so, we explain the variables and the relations between the variables, either by using graphs or mathematical definitions. The constraints modelled are then linked to potential goals they might serve in the context of evolutionary programming.

### Goals

- Theoretically model GAs as CSPs
- Speculate on the benefits of such a formalism
- Experimental part left as future work

## 1. Introduction

Genetic algorithms are known to be used in solving constraint satisfaction problems [G1, G2], especially for the larger class of scheduling problems [G3]. This study is however on a different matter. As such, we attempt to model parts of a genetic algorithm using constraint programming. Later on, we'll see that both the problems of constraint satisfaction, as well as constraint optimization can be used to formalize steps in a generic genetic algorithm.

Whether these models are actually useful in practice remains a matter for further research. Thus, the main goal of this study is to conduct an investigation on which parts of a genetic algorithm could be formalized using constraint programming and then speculate on the benefits of such an approach.

## 2. General goals in evolutionary programming

The general structure of a genetic algorithm is represented by these steps:

- Selection
- Crossover
- Mutation

Genes encoding: various ways, sometimes finite strings assumed

**Fitness**

The process of evolving the population is performed through the use of a chosen fitness function. This function guides the selection of individuals for crossover, as well as the retention of newly obtained individuals to the pool.

**Constraints**

One related subject is the incorporation of constraints in genetic/evolutionary algorithms. Past attempts include [G0, G4, G6]. 

**Viral Infection**

[G0] presents a new kind of operator named infection. Its purpose is to apply mutations (caused by a virus) to parts of the candidate population of solutions, differing from the mutation operator which acts on an individual by individual basis. These viral mutations can enforce simple constraints on the pool of candidates.

**Aging**

Across the genetic algorithms literature, we can find other such nature inspired techniques. For instance [G5] mentions a process similar to aging applied to the candidate population, such that the size of the pool is constrained to avoid increasing the computation time for the selection step across generations.

**Goals**

- generate offspring that represent valid solutions (reduce redundancy)
- different pairs of crossed-over individuals should result in different offspring (maintain diversity)

## 3. Modelling evolutionary goals through constraint programming

While the purpose of genetic algorithms is to maximize a certain fitness function through heuristic methods, constraint satisfaction & optimization modelling allow us to formalize search in a general constrained variable assignment space. Thus we are able to utilze general problem reduction and search strategy algorithms. If we then look back at genetic algorithms, we can see that we can impose similar general constraints in the steps of maximizing a fitness function, namely the selection and the crossover steps.

The selection of a subpopulation of individuals can be transformed into a variable assignment problem with constraints, for instance constraints to include diversity or specific features into the subpopulation. This can be further formalized into a constraint optimization problem, where we maximize some utility function. The crossover step relies on an operator for mixing genes/features. This mixing is also prone to constraints and utility because it can be respresented as a variable assignment problem where we want to discover the best mapping possible for the crossover operator, the one which potentially produces highest fitness individuals.

### 3.1 Constraining Selection: the Pairing Idea

Upon each selection of the crossed-over sub-population, perform pairings of individuals such that:

- each individual is used in a single crossover => variable assignment problem (diversity++ because each set of genes is only used once)

- constraint 1: variable i cannot be assigned label i (unary, similar to x < 3, x > 3)
- constraint 2: variables have different labels (binary, similar to N-queens not attacking on columns)
- constraint 3: if variable i is assigned label l, then variable l must be assigned label i (binary)

**Constraint Graph and Assignments for 4 individuals**

| Constraint Graph for 1 & 2|Assignment Graph Constraints for 1, 2 & 3|
|:--------:|:--------:|
|![Constraint Graph for 1 & 2](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/CG1.png)|![Assignment Constraints for 1, 2 & 3](https://raw.githubusercontent.com/perticascatalin/open_nenos/master/DPML/imgs/CG2.png)|
| Unary constraints integrated in variable domain {}, Binary constraints represented as edges.| Each node represents a valid assignement. +: assignments must occur together. -: assignments must not occur together.|

- we can add additional constraints for having variable i assigned label l, in the sense that genes(i) should not be too similar to genes(l) (diversity++ because we avoid mixing similar data)

Then the problem would be transformed into a constraint satisfaction optimization problem.

**Potential beneficial outcomes of such constraints:**

- increase the diversity of the population
- decrease the redundancy of mainting a high similarity group of individuals

These should occur irrespective of the chosen crossover operator (do not rely on operator specifics).

### 3.2 Constraining Crossover: the Resemblance Idea

Assuming a total possible population of N, or the equivalent to assuming that the given problem has solutions from a finite set, then finding a valid crossover operator can be modelled as assigning labels from the population to variables representing combinations of 2 from the total possible population. Then there are N(N-1)/2 variables to assign. However, there are some which will not be assigned labels, either because we cannot or because this would be inconsistent with the constraints.

The problem is split into an unconstrained or a constrained version based on the assumption of whether to allow an individual to participate in at most 1 pair. We partially formalized this at the selector topic, the extension is as follows:

```
v1 (1, 2) -> 3
v2 (1, 4) -> 2
...
```

or

```
v1 (1, 2) -> 3
v2 (1, 4) -> ∅
...
```

Either way, it is not possible to satisfy 

```
v_1 ≠ v_2 ≠ ... ≠ v_n_n-1/2
```

all of the time in a discrete finite space. This is without disabling certain mappings. However, this makes sense in practice because the population does not span the whole domain.

Besides the constraints imposed on the mapping of combinations to individuals, we also want the mapping to retain features from parent to offspring.

Given a variable `v_i`, we have the following model:

- `N` population & domain for labels assignment
- `V` variables `= N x N`
- `v_i = (a,b)`
- `M : V -> N`
- `p1(v_i) = a`
- `p2(v_i) = b`
- `M(v_i) = c`
- `F : N -> Str(k)` features/genes encoded as a finite string or set

Then the constraints for resemblance (genes transfer) are:

- `F(c) ⋂ F(a) ≠ ∅`
- `F(c) ⋂ F(b) ≠ ∅`

Maybe, but not necessarily `F(a) ⋃ F(b) = F(c)` - no new genetic material. Then mutation can relax this constraint.

Going further, we could enforce on the fitness function: `Fit(c) = some_funct_of(Fit(a), Fit(b))` Then maximizing the fitness function for an assignment can be seen as the maximum utility problem, slightly connected to gene similarity constraint at the selection step.

As for ensuring that the crossover operator maintains consistency, we would need to look into the details of gene encoding, whether sets or strings. This would have to be done based on the specificity of the problem. Since we label all possible solutions as individuals, then a solution is inconsistent when its genes are not consistent wrt. genetic constraints.

A side note that for searching a string in a dictionary we could use a data structure called trie. This trie could be seen as an analogy to the genetic constraints.

**Potential beneficial outcomes of such constraints:**

- control non-determinism of offspring generation and express its fitness as sub-parts of inherited genes fitness (resemblance)
- decrease the redundancy of generating inconsistent solutions (constraints)

These should occur irrespective of the selection step specifics (do not rely on bijective relation).

## 4. Conclusions


### References

- [G0] Solving constraint satisfaction problems by a genetic algorithm adopting viral infection, 1997, H. Kanoh et al., *Engineering Applications of Artificial Intelligence*
- [G1] Solving the Constraint Satisfaction Problem using Genetic Algorithms, 2008, N. Hassan et al., *International Conference on Artificial Intelligence*
- [G2] An Adaptive Genetic Algorithm for Solving N-Queens Problem, 2017, U. Sarkar & S. Nag, *ArXiv: Neural and Evolutionary Computing*
- [G3] A Genetic Algorithm with CSP for multi-objective Optimization in Workflow Scheduling, 2013, J. Sublime et al., *International Journal of Metaheuristics*
- [G4] Evolutionary Algorithms and Constraint Satisfaction: Definitions, Survey, Methodology, and Research Directions, 2001, A.E. Eiben, *Theoretical Aspects of Evolutionary Computing. Natural Computing Series*
- [G5] Comparative Performances of Crossover Functions in Genetic Algorithms, 2015, M. I. Ezeani et al., *International Journal of Scientific & Engineering Research*
- [G6] Genetic Algorithms in Constrained Optimization, 1996, D. J. Reid, *Mathematical and Computer Modelling*