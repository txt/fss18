# Axe = argmin, argmax of X


`ArgMin(d,x,list)` and `ArgMax(d,x,list)`
are functions that seek the value of element  `a=list[i]`  that minimizes/maximizes the expected value of 
the function `x(a)` above and below that element.

This process is then repeated recursviely `d` times on each part of the data.

A large number of learners, clusterers, evaluation methods can be characeterised in this way.


## Example1

For example, given the numbers

    100,10,90,20,110,30,90,40,120

we might what to know how to best split the numbers so as to minimize standard deviation.

Step1: sort the numbers:

    all= 10,20,30,40,90,100,110,120
      i= 1  2  3  4  5  6   7   8

Step2: what is `f` of the whole space?

    all.n  = 8
    all.mu = 65
    all.sd = sqrt( sum( (all[i] - all.mu)^2 ) / (n-1) ) = 44.4

Step3: find any split (say,i=2) and calculate the standard deviation above and below that slot

    left     = all[ i <= 2 ]
    right    = all[ i >  2 ]
    left.sd  = 7.07
    right.sd = 37.64

Step 4: find the expected value of the standard deviation afer the split.

    xpect(n, n1, v1, n2, v2) = n1/n*v1 + n2/n * v2
    left.n   = 2
    right.n  = 6
    xpect(8, left.n, left.sd, right.n, right.sd) =  30.00

From this we can conclude that splitting at x=2 will reduce the uncertainty in this space from 44.4 to 30. Great!

Step5: now repeat the above, but for all values of `i`. 

- For sanity sake, we might demand that each left and right split
not be too small; e.g. `enough=2` items. 
- We'll also assume there exists some `Num` class that can incrementally update and report `n` and `sd`.

Here's `ArgMin(1,sd, list)`; i.e. only one level of split and we want to minimize standard deviation:

```python
def sd(x, y): 
  return xpect(x.n + y.n, x.n, x.sd, y.n, y.sd)

def lt(x, y): return x < y
def gt(x, y): return x > y

def xSplit(lst, 
          lo    = 1, 
          hi    = length(lst), 
          enough= 2, 
          better= lt, 
          f     = sd,
          best  = 10000000):
  cut = nil
  if hi-lo > 2*enough: # otherwise, why bother?
    left  = Num()
    right = Num()
    for i = lo, hi: 
      right + lst[i] # give eveything to right
    for i = lo, hi:
      a = lst[i]
      left  + a   # add one to the right
      right - a   # remove one from the left
      if left.n >= enough and right.n >= enough:
        tmp = f(left,right)
        if better( tmp , best ):             
          cut, best = i, tmp
  return cut,best
```

Note that:

- This function returns `cut=nil` if no cut is found.
- This function assumes the list is sorted before calling this function.
- For Python use `lo,hi = 0` to `length-1`;
- If you want to generate more than one split, then call it recursively
  with `lo=lo,hi=cut` and `lo=cut+1,hi=hi` and `best` (in the 
  recursive call) equal to the `best` return from the above).
- To minimze on other things then use another `xpect`
  function.
- This can actually serve as a `argmax` as well.
    - Change `better` to `gt`
    - Initialize `best` to a large negative number.

 
If we called this in the above data, then it would recommend we cut at 4,
i.e. the list

    all= 10,20,30,40,90,100,110,120
      i= 1  2  3  4  5  6   7   8

should split into 

    left = 10,20,30,40
    right= 90,100,110,120

So what we have right now is a very simple 1-dimensional clustering algorithm for a list of numeric numbers

For lists of more complex data types, we need to pass in a selector, which we will call `x` that extracts the number we want to use from each
item in the list. E.g. if clustering on an Employee's age, we might use `x=employee.age`.

Further, given tables of independent and dependent variables, sometimes we want to clsuter on the independent variable in order to
have most impact on the dependent variable.
e.g. age alive

sanity checks Sanit.g.y checks. sd cohen. fayyad iranni. is it valid to split (are the splits actually different?)

scott knott 

FFTtrees

which would have an expected value of standard deviation of 12.9 (much less than the origianl 44.4)   

def gotEnd(x, y) 
  return xpect(x.n + y.n, x.n, x.ent, y.n, y.ent)
