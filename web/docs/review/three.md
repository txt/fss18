# REVIEWS 3 and 4

The questions that follow are based on the lecture topics listed below

1. Week 3: [Domination](https://txt.github.io/fss18/lectures/domination/)
2. Week 4:  [Statistics](https://txt.github.io/fss18/lectures/stats/)


## Domination

- What is a Pareto frontier?
- Give a framework for a general evolutionary algorithm
- List some of the domination methods used in multi-objective optimization
- How does binary domination work?
- How does indicator based domination work?
- In the following example, we are attempting to (a) minimize Objective-1, (b) minimize Objective-2, and (c) Maximize Objective-3. For this case, would binary domination work?
	+ If yes, list the non-dominated rows.
	+ If no, explain why.
```
		Row ID	Objective-1 	Objective-2 	Objective-3
		1       10             15           20
		2       12             20           22
		3        8             18           20
```
- How is the `dom` score computed in indicator based domination?
	+ True/False: Lower the `dom` score, the better.
- In the following example, we are attempting to (a) minimize Objective-1, (b) minimize Objective-2, and (c) Maximize Objective-3. 	
	+ Compute the `dom` score.
	+ Sort rows based on the `dom` score
```
		%cylinders   <weight   >acceltn   >mpg
		8            4425      11         11
		8            4955      11.5       10
		8            4464      11.5       10
		8	         4464      12.5       10
		4            1985      21.5       40
		4            2085      21.7       40
		4            2130      24.6       40
```

## Evaluation measures for predictors
1. Define (with corresponding formulae) the following measures
  + RE, MRE, MMRE, medMRE, PRED(30).

## Statistics

1. Define and distinguish the following:
	- Effect size and Significance tests
	- Parametric, Non-Parametric tests
2. Cohen's delta is a non-parametric effect size test. Explain.
3. Explain this statement in terms of gaussian distribution: "Any significance test reflects on the overlap between distributions"
4. For question 3 (above), draw 3 diagrams with pairs of distributions depicting the differences
5. Explain how the Scott-Knott test works.
6. In the innermost loop of scott-knott test, what kind of hypothesis would you apply?
7. What are the similarities between scott-knott tests and unsupervised discretization
8. What are the differences between scott-knott tests and unsupervised discretization

## K-NN

1. KNN is called a lazy learner (and decision tree learners are not lazy). Why?
2. KNN is called an instance-based learner (while decision trees are model-based). Why?
3. Explain the following statements
  + KNN can be simply extended to steam mining while decision trees, not so much.
 	+ KNN is faster than decision trees, for training, but very much slower when tested on new data.
	+ When k=1, the kernel function is irrelevant.
	+ KNN can be optimized with some stochastic sampling
	+ Any stochastic sampling method has to be certified with experimentation
4. What does the kernel function do in KNN?
5. What are linear, median, triangular kernels? Explain with a numeric example.
