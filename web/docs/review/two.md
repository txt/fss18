# Review 2

## General Questions

*   What constitutes a good baseline? (Hint: See lecture notes on baselines)
    *   Enumerate the categories and provide a one line description.
*   What is a pareto frontier?
    *   True/False -- There exists a pareto frontier for 1-objective problem
    *   True/False -- An n-objective optimizer has an n-dimensional pareto frontier
*   How does Naive Bayes work?
    *   What are the merits and demerits
*   What family of data mining methods would you use for these cases?

```
    No. classes |  Symbolic  | Numerics |
    ------------|------------|----------|--
    = 1         |            |          |
    ------------|------------|----------|--
    > 1         |            |          |
    ------------|------------|----------|--
    a range     |            |          |
    ------------|------------|----------|--
```

*   Discuss some strategies to obtain a class value while performing kNN for
  	* A symbolic class (True or False)
	* A numeric class (where values falls between 0 to 1)
	* No class variable

```
		@relation weather

		@attribute outlook {sunny, overcast, rainy}
		@attribute temperature real
		@attribute humidity real
		@attribute windy {TRUE, FALSE}
		@attribute play {yes, no}

		@data
		sunny,85,85,FALSE,no
		sunny,80,90,TRUE,no
		overcast,83,86,FALSE,yes
		rainy,70,96,FALSE,yes
		rainy,68,80,FALSE,yes
		rainy,65,70,TRUE,no
		overcast,64,65,TRUE,yes
		sunny,72,95,FALSE,no
		sunny,69,70,FALSE,yes
		rainy,75,80,FALSE,yes
		sunny,75,70,TRUE,yes
		overcast,72,90,TRUE,yes
		overcast,81,75,FALSE,yes
		rainy,71,91,TRUE,no

```

Using the above example, answer the following questions:

*   On variable types:
    *   What is symbolic variables? Please give 2 examples.
    *   What is numeric variables? Please give 2 examples.
    *   Name one operation that can be performed on both numeric and symbolic variables.
    *   Name one operation that can be performed on numeric but not symbolic variables.
    *   How do you calculate the distance between symbolic variables? Please give 1 example.
    *   How do you calculate the distance between numeric variables? Please give 1 example.
    *   What is normalization? Why might it be useful?
    *   In the above data, normalize temperature=65, humidity=70
*   On Independent variables:
    *   What is independent variable? Given an example
    *   What's the difference between decision tree and random forest?
*   On Impurity:
    *   What is the connection between variance and standard deviation?
    *   What is the same about variance and entropy?
    *   What is difference between variane and entropy?
    *   How do we calculate entropy? What is the entropy of `play?` Show your working.
    *   How do we calculate standard deviation? What is the standard deviation of `temperature`? Show your working.
    *   Note: The Gini Index is used to compute the impurity of a data partition. It is computed as 1 - (∑ (p.i)^2). For example, assume the data partition D consisiting of 4 classes each with equal probability. Then the Gini Index (Gini Impurity) will be: Gini(D) = 1 - (0.25^2 + 0.25^2 + 0.25^2 + 0.25^2)
    *   Is Gini defined for symbolic or number variables?
*   On Dependent variables:
    *   Define a dependent variable. Given an example.
    *   What the difference between supervised and unsupervised learning? Please give 2 example tasks for each of them.
    *   In classification taskes, is the dependent variable numeric or symbolic? What about regressions?
    *   If there are more than one numeric class variable, what kind of problem do we have?
*   On Decision Tree learning:
    *   Decision tree is often called "iterative dichomization". Why?
    *   In the following decision tree, `outlook` is the top split and `temperature` never appears in the tree. Why could that be?
    *   For the golf dataset above, do the following, show all your calculations and explainations:
        *   calculate the entropy of the class variables.
        *   calculate the expected value of the entropy of the class symbol after splitting on `outlook`.
        *   calculate the expected value of the entropy of the class symbol after splitting on `temperature`.
        *   compare the three values. What can you say?

```
    outlook = sunny
    |   humidity = high: no
    |   humidity = normal: yes
    outlook = overcast: yes
    outlook = rainy
    |   windy = TRUE: no
    |   windy = FALSE: yes
```

## Python Stuff

*   What is the airspeed velocity of an unladen swallow?
*   What does `yield` do?
    *   How is it different from a `return`?
*   What is the purpose of a context manager?
*   Given the following code, explain what happens with respect to context manager-

```python

    with open(f, 'w') as fname:
        "do some thing"
        "do some more things"
```

*   Match the following regex terms to their tasks `fill-up-this`
*   Explain the following regex operation. Specfically, what happens to the string variable `a_text_string` in the following snippet-


```python

		re.sub(r'([ \n\r\t]|#.* )', "", a_text_string)

```

*   Give an example of a ternary operator in python.
*   What does the `enumerate` operation do in python?
*   Explain what's going on here-

```python

		[a[i] for i, user in enumerate(users) if user==True]

```
