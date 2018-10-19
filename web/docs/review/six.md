# REVIEW 6

- Define the following goals (for numeric goals) and give examples of each
    - RE
    - MRE
    - PRED(30)
    - medianRE
    - standardized accuracy
- The following diagram challenges the idea that correlation is a good assessment measure for numeric goals. What is being said here? Why is it important?



<img width=400 src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/990px-Anscombe%27s_quartet_3.svg.png">

-----

Conisder the following example1:

```
  no,  yes,   <-- classified as
 1000,  10,   no
  20,    1,   yes
```

For example1:
- calculate accraucy and recall and precision and distance to heaven for the "yes" class.
- explain: "accurate models aren't" (for imbalanced data).

-----

Consider the following example2:


```
apples,   beans,    carrots,  <-- classifieed as
50,       10,          5,    apples
 5,       80,         10,    beans
20,       30,        100,    carrots
```

For example2:

- Calculate precision(apples) and  false alarms (carrors)

------

Consider the following example3


```
apples,   beans,    carrots,  <-- classifieed as
50,        0,          0,    apples
 0,       80,          0,    beans
 0,        0,        100,    carrots
```


For example3:

- Explain why we might be a little suspicious of this result.

----

Draw a standard ROC curve (labelling each each):

- Mark "heaven" on your curve
-  Explain the "no information line".


Explain the intuition (but do not define mathematically), behind the following:

- Popt20
- IFA

A client demands a high recall detector with no false alarms:

- What might you try to explain to them?
