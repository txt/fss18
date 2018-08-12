

# hyperpipes, again

crazy simple. this time, cluster data first

# fast lazy learning

use LSH to express all rows as N bits

- does it make NN faster?

use the same bits for topdown clustering

- pick that bit that most evenly divides the data
- or that minimzing variance of goal score in each div

prune the tree

- no sig change between goal score in leaves

find leaves l1,l2 where l2 significantly improves, degrades l1

- generate contrast sets (bore) for each

play with data reduction: 

- only keep n items for each bit patterns
- only keep a sumamry for each bit pattern

do reverseNN. keep only the protypes. use FFT to report deltas
beteen the prototypes


list the baseline

- staochasit needed to see change
     - detect stability
     - need an update method, need minimal updates

