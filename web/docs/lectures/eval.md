# Evaluation
XXX must show SA

## Re-run on Multiple Samples

###  e.g. cross-val

Divide into "_x_ bins

- Test on one bin, train on the others
- Runs the risk of using future data
  to train for testing on the past

Using combined with some stochastic re-orderings

- So "_M_" times, randomly rarrange order of data
- Then do an "_N_"-way cross val for each order
- Avoids "order effects" where the results are  some quirky result based on the order of data colelction/generation.

M=N=10 is common

- but I've never seen the point for more than M=N=5.

### e.g. round robin

- Given N projects
- Train on N-1, test on the nth.
- e.g [Github issue close time, Table4](https://arxiv.org/pdf/1702.07735.pdf)

###  e.g. incremental validation. 

- Divide into "_x_" buckets, 
- Train on buckets 1..i, test on i+1



http://www.cs.le.ac.uk/people/llm11/publications/MinkuYaoICSE14.pdf


###  e.g. moving validation. 

- Divide into "_x_"
        buckets, 
- learn on buckets i..i+n, test
	on i+n+1. eg. Krishna's K-test.

### e.g. RRS (repeated random streaming)

- e.g. repeatedly stream over the data, 
- each time using n% of the data selected at random
- Q: What "n"? 
- A: Engineering judgement 

## BTW, Beyond "Evaluation"

Evaluation can be so tedious and time-consuming that many researchers have asked
if all that inference can be applied to improving the model:

- So "evaluation" becomes "improvement" or "monitor and repair"

- Cross val to ensembles to bagging to boosting

- Round robin
to transfer learning 

- Anomaly detection
to repair 

### Incremental learning

SAWTOOTH: Dumb as all hell

Active learning

- uncertainty sampling
- certainty sampling

Bayesian Parameter optimization (widely used)

FLASH
