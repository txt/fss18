# REVIEW 5

The questions that follow are based on

1. Tools: Scikit-Learn
2. Tools: NLTK


## Scikit Learn

- Why is it a good idea to shuffle your training data?
- When could shuffling be a bad idea? Give 2 examples.
- What is a Binary classifier? How is it different from an `n-ary` classifier?
- What is a confusion matrix
- Write a snippet to obtain the confusion matrix from Scikit learn
- In the above confusion matrix that you obtained from scikit-learn, what do each of the cells represent. In other words, fill the following matrix:

```
--|-------------|-------------------|------------------|--
  |             |        ?=?        |        ?=?       |
--|-------------|-------------------|------------------|--
  |     ?=?     |         ?         |         ?        |
--|-------------|-------------------|------------------|--
  |     ?=?     |         ?         |         ?        |
--|-------------|-------------------|------------------|--
```
- With the above confusion matrix, write a snippet to compute:
	-	Precision
	- Recall
	- False Alarm
	- F1 score
- What is a k-fold cross validation?
- What is stratification? Why is used?
- When would k-fold cross-validation be misleading?
- How would one convert a linear regression into a binary classifier?
- What is a decision hyperplane?
- Say you have an n-dimensional data, how many dimensions would the decision hyperplane comprise of?
- What is the key intuition in SVM?
- What does an SVM aim to achieve when training?
- SVM seem to work very well for which domain? (Ans: Text Classification)
- What are hyper-parameters?
- What is the difference between CART and Random Forest?
- How does Random Forests work?
- What is a `mode` of an array?

## Text Classification

- Draw a general pipeline for a simple text classification task.
- Define in a sentence or two, what each of the blocks above aim to achieve.
- Define the following terms:
	* Tokenization
	* Lemmatization
	* Stopword removal
	* Part-of-speech tagging.
- Given a sentence below, convert it into tokens using: Tokenization, Lemmatization, and Stopword removal.
	* "This is a sentence about cats"
- What is vectorization?
- Give the mathematical formulation of the following:
	* Term Frequency
	* Document Frequency
- What is intuition underlying TFIDF vectorization?
- Generate a TFIDF vectorization of the following two sentences:
	1. "Something about a cat."
	2. "Something about a dog."
- How does sk-learn store sparse matrices? (Ans: CSR Format)
- What is the CSR (compressed sparse row) format?

## Multiprocessing
- What is Global Interpreter Lock (GIL)?
- What is chunking?
- Distinguish between synchronous and asynchronous processes.
- How would you count the number of processors in your system with python's Multiprocessing?
- Write a snippet to print "Hello, World! {processor id}" on each of the systems processors.
