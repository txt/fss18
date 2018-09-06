# Potential Ideas For Class Projects


## Anomaly Detection
 + If the performance is not what you'd expect, then that is an anomaly.
 + How would you detect anomalies in SE data?
 + What is the current state-of-the-art?
 + How about measures like Heoffding Bounds?
 + How about something like kNN on the leaves of a decision tree?
 + Other ideas enouraged ... 

## Explanation vs. Performance of Decision Trees
 + Decisions Trees can be limited to any depth?
 + How does restricting the depth of the tree effect performance (see Holte 1R) for binary classes? For n-ary classes?
 + If we had a model in an incomprehensible  format (that of say NB, deep learning, neural net) and we ran the training data through decisions trees, what is the performance vs explanation tradeoff?
 + How do we quantify explanations? 
    - https://arxiv.org/pdf/1803.05067.pdf
    - https://link.springer.com/article/10.1007/s10664-018-9638-1

## FLASH for tuning Defect Prediction
 + Look at Vivek Nair's [TSE article on FLASH](https://arxiv.org/pdf/1801.02175.pdf)
 + Can you apply this to construct better defect predictors?
 + Can you tune defect predictors for better precision, false alarm, recall?

## FLASH for effort estimation?
 + Same as above, but this time for effort estimation.

## Can you beat FLASH with Baysian Parameter Optimization
 + What are the tradeoffs with using BPO

## Reasoning over instance-based evolutionary algorithms
 + Pick a task to optimize over (tuning defect predictors for example)
 + Cache generation zero of an evolutionary algorithm (say DE)
 + Run the algorithm 
 + Cache generation N of the same algorithm
 + Run a rule learner over the generations to learn rules about the most
   informative features.
 + Questions 
   - How good is that learner at selecting for best (last gen) instances?
   - How much is that goodness effected by sampling from how much of non-best?

## Develop better evolutionary algorithms
 + Experiment with mutation strategy
 + Parallelize the algorithm
 + Other ideas?

## Scalable planning with XTREE
 + Look at Rahul Krishna's paper on [XTREE](https://arxiv.org/pdf/1708.05442.pdf)
 + This currently works on smaller datasets, can you create a scalable
   implementation of this that works on a streaming data?
 + Use ideas from Very Fast Decision Trees: https://homes.cs.washington.edu/~pedrod/papers/kdd00.pdf
