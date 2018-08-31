# Review1

+ What is NFL? What are its implications for selecting the "best" learner
+ List 5 baseline criteria for an AI tools, make argument:
    - Why it is important to meet that criteria?
    - Why, pragmatically, it might be necessary to ignore (or, at least relax) that criteria
+ Distinguish supervised (S) from unsupervised (U) learning
    - When would do S or U?
    - Is FFT an S or U? Why? (Hint: your answer should say something about FFT). 
    - Is the Fastmap Cluster an S or U? Why? (Hint: your answer should say something about the Fastmap clusterer). 
+ Instance models refer to specific values  (e.g. X=6,Y=10,Z=100) while other models  refer to ranges of some attributes (e.g. _X>6_ and _Y < 5_).
    - Which of these models reference _points_ or _volumes_?
    - Which of these offer more generalizations of the past?
    - Which of these are shorter to share?
    - How to generalize from point models to models that cover volumes?
- FFTs:
    - What are the attributes in an node of an FFT tree?
    - What is the structure of an FFT tree (hint: use the node attributes to make that description).
- Fastmap Clustering
    - Given 2 points _Y,Z_ at distance _c_, if a new point _X_ is _a=dist(X,Y)_ and _b=dist(X,Z)_, derive
      an expression for the distance _x_ that _X_ falls along the line between _Y,Z_.
    - What are the attributes in an node of an Fastmap cluster? (hint: parts of it are recursive)
    - What is the structure of an Fastmap clustering tree (hint: use the node attributes to make that description).
    - How to use a Fastmap cluster node for 
         - classification (hint: there are many ways)
	 - anomaly detection, sharing,  privacy ([hint: see III.D.4](http://menzies.us/pdf/15lace2.pdf)
         - incremental model updates over an infinite stream of data? ([hint](https://ai-at-wvu.blogspot.com/2010/01/simple-single-pass-k-means.html)
- How to use any clustering method for optimization, anomaly detection, classification, sharing, privacy.
- How to use a Fastmap cluster free for:
         - very fast optimization ([hint: see Algorithm1](https://arxiv.org/pdf/1608.07617.pdf))
- What are diversity measures for numeric and symbolic values? Offer a formula for each.
- What is the diversity of "y,n,y,y,y,n,y,y,n"? If you don't have a calculator, show all working and stop before the final calculation.
- What is the diversity of "10,89,32,11,9,90,30,31,91"? If you don't have a calculator, show all working and stop before the final calculation.
- Consider the following data.
    - Just considering the `age` column, where to divide it such that `age` diversity is minimized?
      Assume a minimum bin size of 3.
    - Now consider the `age,alive` relationship. Where to divide `age` in order to reduce the diversity of `alive`?
      Assume a minimum bin size of 3.

Data:    


     age,alive
     10, y
     89, n
     32, y
     11, y
     9,  y
     90, n
     30, y
     31, y
     91, n

- Iterative dichmotization (ID) algorithms divide attributes into ranges, then recurse on each range. 
    - How do ID algorithms decide what attribute with which  to split the data
