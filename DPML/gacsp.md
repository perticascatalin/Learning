# Constraint Programming in Genetic Algorithms

## Goals

- Theoretically model GAs as CSPs
- Speculate on the benefits of such a formalism

## Introduction

Genetic algorithms are known to be used in solving constraint satisfaction problems [G1, G2], especially for the larger class of scheduling problems [G3]. This study is however on a different matter. As such, we attempt to model parts of a genetic algorithm using constraint programming. Later on, we'll see that both the problems of constraint satisfaction, as well as constraint optimization can be used to formalize steps in a generic genetic algorithm.

Whether these models are actually useful in practice remains a matter for further research. Thus, the main goal of this study is to conduct an investigation on which parts of a genetic algorithm could be formalized using constraint programming and then speculate on the benefits of such an approach.

The general structure of a genetic algorithm is represented by these steps:

- selection
- crossover
- mutation

One related subject is the incorporation of constraints in genetic/evolutionary algorithms. Past attempts include [G0, G4, G6]. 

**Viral Infection**

[G0] presents a new kind of operator named infection. Its purpose is to apply mutations (caused by a virus) to parts of the candidate population of solutions, differing from the mutation operator which acts on an individual by individual basis. These viral mutations can enforce simple constraints on the pool of candidates.

**Aging**

Across the genetic algorithms literature, we can find other such nature inspired techniques. For instance [G5] mentions a process similar to aging applied to the candidate population, such that the size of the pool is constrained to avoid increasing the computation time for the selection step across generations.

The process of evolving the population is performed through the use of a chosen fitness function. This function guides the selection of individuals for crossover, as well as the retention of newly obtained individuals to the pool.

## General goals in evolutionary programming

- generate offspring that represent valid solutions (reduce redundancy)
- different pairs of crossed-over individuals should result in different offspring (maintain diversity)

## Modelling evolutionary goals through constraint programming

Interlink: fitness vs consistency

### Constraining Selection: the Pairing Idea

Upon each selection of the crossed-over sub-population, perform pairings of individuals such that:

- each individual is used in a single crossover => variable assignment problem (diversity++ because each set of genes is only used once)

- constraint 1: variable i cannot be assigned label i (unary, similar to x < 3, x > 3)
- constraint 2: variables have different labels (binary, similar to N-queens not attacking on columns)
- constraint 3: if variable i is assigned label l, then variable l must be assigned label i (binary)

- we can add additional constraints for having variable i assigned label l, in the sense that genes(i) should not be too similar to genes(l) (diversity++ because we avoid mixing similar data)

**Potential beneficial outcomes of such constraints:**

- increase the diversity of the population
- decrease the redundancy of mainting a high similarity group of individuals

These should occur irrespective of the chosen crossover operator (do not rely on operator specifics).

### Constraining Crossover: the Resemblance Idea

- control non-determinism of offspring generation and express its fitness as sub-parts of inherited genes fitness (resemblance)
- decrease the redundancy of generating inconsistent solutions (constraints)

These should occur irrespective of the selection step specifics (do not rely on bijective relation).

## Papers

### G0: Solving constraint satisfaction problems by a genetic algorithm adopting viral infection

1997, H. Kanoh et al.

Engineering Applications of Artificial Intelligence

*Several approximate algorithms have been reported to solve large constraint satisfaction problems (CSPs) in a practical time. While these papers discuss techniques to escape from local optima, the present paper describes a method that actively performs global search. The present method is to improve the rate of search of genetic algorithms using viral infection instead of mutation. The partial solutions of a CSP are considered to be viruses and a population of viruses is created as well as a population of candidate solutions. Search for a solution is conducted by crossover infection substitutes the gene of a virus for the locus decided by the virus. Experimental results using randomly generated CSPs prove that the proposed method is faster than a usual genetic algorithm in finding a solution when the constraint density of a CSP is low.*

### G1: Solving the Constraint Satisfaction Problem using Genetic Algorithms

2008, N. Hassan et al.

International Conference on Artificial Intelligence

*Genetic algorithms are an evolutionary technique that uses selection, crossover, and mutation operators to solve optimization problems using a survival of the fittest idea. In this paper, a straightforward genetic algorithm is used to solve the Constraint Satisfaction Problem (CSP). As many different selection, crossover and mutation operators have been devised, this paper aims to compare three different selection methods, namely, Roulette Wheel Selection, Rank Selection, and Tournament Selection. Two mutation methods are also compared, Reciprocal Mutation and 2-Op Mutation. We concentrate in comparing the results of the genetic algorithm to know the operators best suited for the CSP.*

### G2: An Adaptive Genetic Algorithm for Solving N-Queens Problem

2017, U. Sarkar & S. Nag

ArXiv Neural and Evolutionary Computing

*In this paper a Metaheuristic approach for solving the N-Queens Problem is introduced to find the best possible solution in a reasonable amount of time. Genetic Algorithm is used with a novel fitness function as the Metaheuristic. The aim of N-Queens Problem is to place N queens on an N x N chessboard, in a way so that no queen is in conflict with the others. Chromosome representation and genetic operations like Mutation and Crossover are described in detail. Results show that this approach yields promising and satisfactory results in less time compared to that obtained from the previous approaches for several large values of N.*

### G3: A Genetic Algorithm with CSP for multi-objective Optimization in Workflow Scheduling

2013, J. Sublime et al.

International Journal of Metaheuristics

*Cloud computing is a fast growing technology allowing companies to use on-demand computation, and data services for their everyday needs. The main contribution of this work is to propose a new model of genetic algorithm for the workflow scheduling problem. The algorithm must be capable of: 1) dealing with the multi-objective problem of optimising several quality of service (QoS) variables, namely: computation time, cost, reliability or security; 2) handling a large number of workflow scheduling aspects such as adding constraints on QoS variables (deadlines and budgets); 3) handling hard constraints such as restrictions on task scheduling that the previous algorithms have not addressed. Using data from Amazon elastic compute cloud (EC2) and workflows from the London e-Science Centre; we have compared our algorithm with other scheduling algorithms. Simulation results indicate the efficiency of the proposed metaheuristic both in terms of solution quality and computational time.*

### G4: Evolutionary Algorithms and Constraint Satisfaction: Definitions, Survey, Methodology, and Research Directions

2001, A.E. Eiben

Theoretical Aspects of Evolutionary Computing. Natural Computing Series

*In this tutorial we consider the issue of constraint handling by evolutionary algorithms (EA). We start this study with a categorization of constrained problems and observe that constraint handling is not straightforward in an EA. Namely, the search operators mutation and recombination are ‘blind’ to constraints. Hence, there is no guarantee that if the parents satisfy some constraints the offspring will satisfy them as well. This suggests that the presence of constraints in a problem makes EAs intrinsically unsuited to solve this problem. This should especially hold if there are no objectives but only constraints in the original problem specification — the category of constraint satisfaction problems. A survey of related literature, however, discloses that there are quite a few successful attempts at evolutionary constraint satisfaction. Based on this survey we identify a number of common features in these approaches and arrive at the conclusion that the presence of constraints is not harmful, but rather helpful in that it provides extra information that EAs can utilize. The tutorial is concluded by considering a number of key questions on research methodology and some promising future research directions.*

### G5: Comparative Performances of Crossover Functions in Genetic Algorithms

2015, M. I. Ezeani et al.

International Journal of Scientific & Engineering Research

*Genetic Algorithms have been widely applied to various kinds of optimisation
problems. In this work, a Genetic Algorithm is designed to solve the three
classic numerical optimisation problems – Rastrigin, Schwefel and Griewank. An
experiment to observe the comparative performances of five different
crossover functions was conducted. Also, the possible effect of aging out some
of the old individuals from the population was hinted at. A parameter set
expected to give the optimal performance and a discussion on the design
considerations are presented below.*

### G6: Genetic Algorithms in Constrained Optimization

1996, D. J. Reid

Mathematical and Computer Modelling

*The behavior of the two-point crossover operator, on candidate solutions to an optimization problem that is restricted to integer values and by some set of constraints, is investigated theoretically. This leads to the development of new genetic operators for the case in which the constraint system is linear.*

*The computational difficulty asserted by many optimization problems has lead to exploration of a class of randomized algorithms based on biological adaption. The considerable interest that surrounds these evolutionary algorithms is largely centered on problems that have defied satisfactory illation by traditional means because of badly behaved or noisy objective functions, high dimensionality, or intractable algorithmic complexity. Under such conditions, these alternative methods have often proved invaluable.*

*Despite their attraction, the applicability of evolutionary algorithms has been limited by a deficiency of general techniques to manage constraints, and the difficulty is compounded when the decision variables are discrete. Several new genetic operators are presented here that are guaranteed to preserve the feasibility of discrete aspirant solutions with respect to a system of linear constraints.*

*To avoid performance degradation as the probability of finding a feasible and meaningful information exchange between two candidate solutions decreases, relaxations of the modified genetic crossover operator are also proposed. The effective utilization of these also suggests a manipulation of the genetic algorithm itself, in which the population is evanescently permitted to grow beyond its normal size.*