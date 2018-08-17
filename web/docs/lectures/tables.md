# Different Learners for Different Data

Let us start at the very beginning (a very good place to start). When you read you begin with A-B-C. When you mine, you begin with data.

Different kinds of data miners work best of different kinds of data. Such data may be viewed as tables of examples:

- Tables have one column per feature and one row per example.
- The columns may be numeric (have numbers) or symbolic (contain discrete
  values).
- Also, some columns are goals (things we want to predict using the other
columns).
- Finally, columns may contain missing values.

For example, in text mining, where there is one column per word and one row per document, the columns contain many missing values (since not all words appear in all documents) and there may be hundreds of thousands of columns.

While text mining applications can have many columns, Big Data applications can have any number of columns and millions to billions of rows. 

For such very large datasets, a complete analysis may be impossible. Hence, these might be sampled probabilistically (e.g., using the naive Bayesian algorithm discussed below).

On the other hand, when there are very few rows, data mining may fail since there are too few examples to support summarization. 

For such sparse tables, k- nearest neighbors (kNN) may be best. kNN makes conclusions about new examples by looking at their neighborhood in the space of old examples. Hence, kNN only needs a few (or even only one) similar examples to make conclusions.

If a table has no goal columns, then this is an unsupervised learning problem that might be addressed by (say) finding clusters of similar rows using, say, K- means or expectation maximization. 

An alternate approach, taken by the Apriori
association rule learner, is to assume that every column is a goal and to look for what combinations of any values predict for any combination of any other.

If a table has one goal, then this is a supervised learning problem where the task is to find combinations of values from the other columns that predict for the goal values. Note that for datasets with one discrete goal feature, it is common to call that goal the class of the dataset.


For example, here is a table of data for a simple data mining problem: 

```
outlook, temp,humid,wind,play
-----------------------------
sunny,	  85,	85,	FALSE,	no
sunny,	  80,	90,	TRUE,	  no
overcast,	83,	86,	FALSE,	yes
rainy,	  70,	96,	FALSE,	yes
rainy,	  68,	80,	FALSE,	yes
rainy,	  65,	70,	TRUE,	  no
overcast,	64,	65,	TRUE,	  yes
sunny,	  72,	95,	FALSE,	no
sunny,	  69,	70,	FALSE,	yes
rainy,	  75,	80,	FALSE,	yes
sunny,	  75,	70,	TRUE,	  yes
overcast,	72,	90,	TRUE,	  yes
overcast,	81,	75,	FALSE,	yes
rainy,	  71,	91,	TRUE,	  no
```

In this table, we are trying to predict for the goal of play?, given a record of the weather.

Each row is one example where we did or did not play golf (and the goal of data mining is to find what weather predicts for playing golf).

Note that temp and humidity are numeric columns and there are no missing values.

Such simple tables are characterized by just a few columns and not many rows (say, dozens to thousands). 

Traditionally, such simple data mining problems have been explored by C4.5 and CART. 

However, with some clever sampling of the data, it is possible to scale these traditional learners to Big Data problems.


## Y = F(X)

One way to look at a table of data is an example of some function that computes
columns "_Y_" from input columns "_X_".

## Splits

Another way to look at a table of data is as a source of `Split`s.

- Columns have ranges
- Most ranges are not interesting (not useful for decision making)
- So most columns are not interesting 
     - Standard lesson: need only `sqrt(col)` of the columns (and for text mining data, even fewer)

Sym columns:

- Splits are solo simples or disjunctions

Num columns:

- Splits can be found oh so many ways
