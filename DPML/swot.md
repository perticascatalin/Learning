# Declarative Programming in Machine Learning: Final Essay

## 1. Abstract

## 2. Graded SWOT (metrics)

### 2.1 Time Investment

|Studying|Backtracking|Genetic|Music|Music Theory|Total|
|:------:|:----------:|:-----:|:---:|:----------:|:---:|
|32|6|12|36|8|**94**|

### 2.2 Coding Effort

## 3. Research Topics

### 3.1 Overall Review (synthesis after you detail for each below)

Then versus course objectives (revise lectures)
Versus other topics (eg. program synthesis - DC, reinforcement learning - Chess & Go)

### 3.2 Queens and Knights

- presents 2 classic backtracking problems
- describes how the 2 problems can be represented as variables assignment with constraints
- experiments are developed based on improvements which leverage problem reduction (arc & path consistency) and search strategies (2 x lookahead)
- an analysis is performed by comparing computation time and feasible input sizes (board size)

### 3.3 ! Constraint Programming in Genetic Algorithms

### 3.4 ! Constraint Satisfaction applied to Music

### 3.5 Future work

Neural guided search for music. Somehow use ML instead of hand encoding musical rules / patterns. Drive a search for musical patterns satisfying certain properties. Eg. in case of canon, given the chord progression and a theme, find all combinations of voices playing the theme either forwards or backwards such that overlapping notes from different voices fall within the chord played at the time a note occurs.

## 4. SWOT Analysis

### 4.1 Challenges

- understanding what the course is about
- understanding the scope and purpose of the assignments
- finding enough good related research for the selected topics
- once I selected a topic, the time to develop it and get past the exploratory phase was quite short, and thus the conclusions drawn were mostly a summary of the findings, which do not include results that could be further used by another researcher, and in research it is very important to structure and deliver content that can be useful or can be built upon

### 4.2 Strengths

- learned how to formalize problem constraints in a declarative way
- learned how to better analyze and look for search strategies
- applied constraint satisfaction to several domains
- through a combination of my style, the exploration of domains with less specialized material available (ref. music, but also genetic algorithms) and the constraints of the assignments, I was able to create more original content than I would have been able to through understanding and comparing various existing studies

Keywords:

- original
- constructive (I start with some ideas and I build on top of them, asking new questions and going into details where more understanding is needed)
- ideas well linked (presented ideas were studied enough to make the initial links)
- the selected topics were quite interesting

### 4.3 Weaknesses

- poor comparative analysis for the reports
- background research not so well established either
- implementing queens and knights experiments before understanding well enough the formalism required for the course
- this lead to a weaker mapping between the required methods to be applied (problem reduction, search strategies) and the experiments (implementation)

Keywords:

- underdeveloped analysis
- lacking results for the research reports / or more limited scope (finding & defining the problems)

### 4.4 Opportunities

- For the report on genetic algorithms, I had to apply CSP to genetic algorithms, instead of using genetic algorithms to solve CSPs, which made me look at problems in a different way
- I learned about variable domains, updating domains based on node, arc & path consistency
- Also, how to organize search in different ways, either through domain heuristics or by general methods relying on branch and bound methods, but there is more to learn here since these were only applied in the lab report on chess backtracking problems
- Finding the potential application of CSPs to the canon problem in music, which seems to be an interesting low hanging fruit of research area, although probably without any commercial use, I was not able to find existing research at the level at which it could be, so there could be some interesting discoveries yet to be made

### 4.5 Threats

- The domain of music does not seem widely formalized for computer science, forcing the researcher to dedicate a considerable amount of time to understanding otherwise simple concepts

### 4.6 Impact
