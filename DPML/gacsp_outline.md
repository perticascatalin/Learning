# Constraint Programming in Genetic Algorithms: Outline

The study presents preliminary ideas for applying constraint programming in genetic algorithms. We start by listing some of the goals of evolutionary programming and we link them to related literature in the domain. Then we look at the steps performed in a genetic algorithm and model them using constraint programming toward facilitating the goals of genetic algorithms.

We come up with 2 main ideas: the pairing idea, for modelling the selection step (as a constraint problem) in order to increase diversity in the population; and the resemblance idea, for modelling the crossover step (as a constraint problem) in order to satisfy the preservation of features from one generation to another.

In both of the above cases, we model the steps as variable assignment problems where there are constraints between variables (CSPs). We emphasize what the constraints are and leave some hints on how to model them as (CSOPs). 