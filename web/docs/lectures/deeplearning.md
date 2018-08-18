# Deep learning

![](https://cdn-images-1.medium.com/max/800/1*dnvGC-PORSoCo7VXT3PV_A.png)

DP is a kind of neural net architecture where the outputs on N i become the inputs to net i+1. 
Deep learning methods are representation-learning methods with multiple levels of representation, obtained by composing simple but non-linear modules that each transforms the representation at one level (starting with the raw input) into a representation at a higher, slightly more abstract level. Compared to the conventional machine learning algorithms, deep learning methods are very good at exploring high-dimensional data.


DL has received a  lot of press lately. 

A. Lot. Of. Press.

The computational requirements for this method are challenging. 
One NCSU grad student working at Google this summer was running 3 years of CPU per day (no joke) for his
DL experiments. While that that is certainly an extreme example, it does illustrate how costly it can be to tune DL networks. Literally, costly. We
costed out one project where 4 students would use commercial GPU clusters to run 20 experiments per week for 3 years. That work would add $1M to the cost
of that grant.

So it seem  DL is the answer, what was the question? If we ask what kind of learners do we need, then work backwards from there, do we get to DL?

Perhaps not. 
[Wolpert](https://ubiquity.acm.org/article.cfm?id=2555237)
reports in his famous No Free Lunch
Theorems that if some learner works best for some data, then some
other earner [will work best for other
data](https://en.wikipedia.org/wiki/No_free_lunch_theorem#Example). Which means that when
DL is not the one solution to all problems. Rather, it is one amongst many that we need to try.


For example, suppose we don't need a classifier, but a planner. In that case, DL might become part of a larger system than uses some classifier as a what-if query device to test different plans.

And if we want an explanation system, then we 'd have to use some symbolic method to run over the same examples as DL to build a second model (and its that model we can show to users). 

Of course, sometimes DL is necessary. Some domains have such frighteningly complex data that layers of neural networks are required to tease out the complexities of the data.

But sometimes, DL is not necessary. And in that case, it seems silly to incur the  computational cost of DL. So far, in SE, the case for the superiority of DL other
other methods has not been made:

- [Are Deep Neural Networks the Best Choice for Modeling Source Code?](http://web.cs.ucdavis.edu/~devanbu/isDLgood.pdf)
- [Easy over Hard: A Case Study on Deep Learning](https://arxiv.org/pdf/1703.00133.pdf)
- [500+ Faster than Deep Learning](https://arxiv.org/pdf/1802.05319.pdf)
