<img src="../../img/ncstate.png" align=right width=300><br clear=right>
<img src="http://ai4se.net/img/ncsu-logo.png" align=right width=100>
# Bad Smells for AI Software

What software engineering principles should we apply
to AI?

- Pressing question;
     - As society uses more AI, SE folks will be required to us and maintain and extend that software
     - What are the _bad smells_ of an AI system that would
  movitate reorganizing that code?

## A Little History

SE's past is full of cases where

- someone said "X" is not part of AI
- then we ignored them and added "X" to SE
- and lots of things got lots better

## Baseline Tools

No 

## Other Requirements

### No eval tools 

Tests conclusion stability

- across mulitple data sets (if
  avaialable) 
- or across multiple subsets of know scenarios

Some examples of that kind of evaluation follow. 

- Note that these can significantly increase the computational cost of using learners. 
- Hence, the need to [faster](faster), [lighter](lighter) AI algorithms. 

####  e.g. cross-val

- Divide into "_x_ bins
- Test on one bin, train on the others
- Runs the risk of using future data
  to train for testing on the past

#### e.g. round robin

- Given N projects
- Train on N-1, test on the nth.
- e.g [Github issue close time, Table4](https://arxiv.org/pdf/1702.07735.pdf)

####  e.g. incremental validation. 

- Divide into "_x_" buckets, 
- Train on buckets 1..i, test on i+1

####  e.g. moving validation. 

- Divide into "_x_"
        buckets, 
- learn on buckets i..i+n, test
	on i+n+1. eg. Krishna's K-test.

#### e.g. RRS (repeated random streaming)

- e.g. repeatedly stream over the data, 
- each time using n% of the data selected at random
- Q: What "n"? 
- A: Engineering judgement 

## No stats tests

- Check if _this_ treatment has
   same effect as _that_ treatment.
- Need at least two tests: 
         [significance](../gloss/significance)  and [effect size](../gloss/effectsize)
- I also think you need a third test;
    - Something
       that clusters the treatments before the other
       tests are applied 
    - Reduces
      the number of other statistical tests. 
   - E.g
       the [Scott-Knot](../gloss/sk.md) test.
