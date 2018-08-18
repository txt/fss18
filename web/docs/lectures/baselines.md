# Baseline for an "Adequate" AI

Software engineering is about engineering and engineering is about
generate a produce of adequate quality, given the available constraints.
What does that mean for AI-enhanced software?

Within any optimizer or data mining toolkit
we can find hundreds of classifiers, regression tools, neural nets, support
vector machines, evlutioanry algorithms, ant-colony optimizers, etc etc, etc.
These primtives can be combined in millions of ways, then tuned in quadrillions of ways  (see the very active research literature
on all these methods). 
So given a new problem, which learner/optimizer should we apply? 

This is a very hard problem. [Wolpert](https://ubiquity.acm.org/article.cfm?id=2555237)
reports in his famous No Free Lunch
Theorems that if some optimizer/learner works best for some data, then some
other optimizer/learner [will work best for other
data](https://en.wikipedia.org/wiki/No_free_lunch_theorem#Example). This means that when
new data arrives, you need _comissioning experiments_; i.e. try a variery of techniques before you can
find what workds best for the local data.

<p class=note>(Aside: it turns out that the NFL has some good news for us: 
the greater the performance gain desired,
<a href="http://www.cs.cmu.edu/~gmontane/pdfs/montanez-2013-bounding.pdf">
the fewer the learners  exist that produce
at least such a performance gain</a>.
See the <a href="https://arxiv.org/abs/1603.06560">Hyperband optimizer</a> for
an adapative approach to pruning away less-than-great methods.
Also, for many learners/optimizers, their
performance is indistinguishable for anything less than some &epsilon; value.
So if we divide the output space into bins of width &epsilon;
means we can stop looking once we find a few methods that 
<a href="https://arxiv.org/pdf/1803.04608.pdf">falls into the best &epsilon; bins</a>.)</p>

When conducting such commissioning experiments, it is methodologically useful to have a _baseline method_; i.e. an algorithm which can generate floor performance values. Such baselines let a developer quickly rule out any method that falls “below the floor”. With this, researchers and industrial practitioners can achieve fast early results, while also gaining some guidance in all their subsequent experimentation (specifically: “try to beat the baseline”).

Using baselines for analyzing algorithms has been endorsed by several
experienced researchers:

- In his [textbook on empirical
methods for artificial intelligence](pdf/empiricalAI.pdf), Cohen
strongly recommends comparing supposedly sophisticated systems
against simpler alternatives. In the machine learning community,
- Holte  uses the [OneR baseline
algorithm](https://www.mlpack.org/papers/ds.pdf) 
as a scout that runs
ahead of a more complicated learners as a way to judge the complexity
of up-coming tasks. 
- In the software engineering community, Sarro et al
et al.  recently proposed [baseline methods for effort
estimation](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.8862&rep=rep1&type=pdf).
- Shepperd and Macdonnel argue convincingly that 
measurements
are best viewed as [ratios compared to measurements taken from some
minimal baseline
system](https://bura.brunel.ac.uk/bitstream/2438/6473/4/IST_Invited_2011_v7.pdf). 
- Work on cross-versus within-company cost
estimation has also recommended the use of some [very simple
baseline](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.8862&rep=rep1&type=pdf)
- I've offered several good baseline AI tools for SE tasks. In both the
  following, my graduate students were able to replace widely used very complex
  solutions with much simple alternative. For example:
    - Data mining: [Bellwethers: A Baseline Method For Transfer Learning](https://arxiv.org/pdf/1703.06218)
    - Optimizing: ["Sampling"' as a Baseline Optimizer for Search-based Software Engineering](https://arxiv.org/pdf/1608.07617)



So for this subject, we propose replacing the question of "what AI tool is best"
with two other questions that make more sense to engineers racing to deliver
products with limited time and resources:

- How can we quickly comission an initial, adequate, AI baseline system?
- What can we do to test and improve on that baseline?


## But what is a "good" baseline?


Here's one list of what a "baseline" means, from [Sarro, TOSEM'18](http://www0.cs.ucl.ac.uk/staff/F.Sarro/resource/papers/SarroTOSEM18.pdf),
which we extend with our own notes. 

<p class=note>The key thing to note about the following is that one system may not satisfy
all these criteria (in fact, no known system satisfied all of them). That said,
 each
of the following points is important. And by reflecting on the value of each
point
for a particular AI application, we naturally consider and review (and possibly
discard) design alternatives.
Which is no bad thing.<br>
&nbsp;<br>

Also, the following list offers a roadmap for future research in SE+AI. Find
  cases where some of these points do not matter. Find ways to enhance
  existing systems such that they perform better on the following criteria.
  Etc.</p>


### The Checklist
   
- SIMPLE: Be simple to describe, implement, and interpret (i.e. interpret the output for business uses).
- STABLE: Be <strike>deterministic</strike> stable in its outcomes
    - I've replaced deterministic with stable, sicne I think that is more
      important.  
    - For example:
        - [Here](http://menzies.us/pdf/12gense.pdf), 
          Fig1, are the coeffectivents learned by regression on 20
           67% samples of some training data. Note their WILD instability.
- INUTIAITVE: Be applicable to mixed qualitative and quantitative data.
    - It is good to use numeric and symblic data.
    - It is useful to be able to initial a systems with qualitative intuitions.
        - Then, at least, you can compare the output to what folks already
          believe.
              - But be warned, in SE, the beliefs of many developers are...
                [dubious](http://web.cs.ucdavis.edu/~devanbu/belief+evidence.pdf).
    - It is useful to be able to guide model construction via high-level qualitative goals.
    - One useful technology here are [Bayes nets](https://www.eecs.qmul.ac.uk/~norman/papers/fentonMMR_Full_v1_0.pdf) which can be either initially
      drawn by people, then revised by data miners, or vice versa.
- GENERAL: Offer some explanatory information regarding the prediction
  by representing generalised properties of the underlying data.
    - Many systems offer only "point" solutions; i.e. examples of what might be useful.
        - Given _N_ attributes, a point solution offers exact values for all attributes.
        - E.g. A happy author might be editting this particular file and this particular time and place. 
    - Some systems offer solutions that hold over a volume;
        - I.e. they ignore some values while saying things like _x > 10_ for
          others.
        - E.g. Happy authors might be editting html files on many computers
          (and when they do it does not matter).
- NO MAGIC: Have no magic parameters within the modelling process that require tuning. 
    - E.g. for random forests, engineers have to decide on how many trees are
      included in the forest.
    - Alternatively, if such tunings exist, then the must be some automatic method for selecting what
      tunings are best for particular data sets.
- AVAILABLE: Be publicly available via a reference implementation and associated environment for execution.
    - In this day and age of Docker images and package managers and Github-like
      environments where everyone can load up each ooher's
      code at the drop of a hat, it makes no sense for some baseline tool to be
      inaccessible.
- USEFUL: Generally be more accurate than a random guess or (e.g. an estimate based purely on the distribution of the response variable).
- CHEAP: Do not be expensive to apply.
    - Here we mean that the CPU, Ram, and disk space required to make something
      work is not crazy high.
- REASONABLE: Offer comparable performance to standard methods.
- ROBUST: I.e. does not change much over different data splits and validation
  methods?
    - And if it does vary wildly, can it find ways to find regions in the data
      where the data conclusions are stable?

Other desirable features are:

- HUMBLE:  cerfication enveiope
- ICREMENTAL:


The project of this class is to apply the above to AI tools applied to SE
problemes. Even trying to apply the above
and not getting anywhere, would also be fine (just as you long as
you document your comprehension of the ideas of baselines,  along the way). 
So go seek, or build, good baselines:

- Take any SE problem and ask are
the current methods "baselines?". Would simpler alternatives suffice? 
- Can you make the method simpler to use; 
    - e.g. replace it with somethign much simpler to implement and explain
    - e.g. apply an optimizer to a data mining to find better settings from that
data miner? 
- Can you make the method use less RAM or be faster to use; 
    - e.g. see what happens if you learn on just X% of the data (randomly
      selected) for    
      X &isin; {50,25,10,5,1}%?
    - If you apply a prototype generator, can you select/build a very small
      subset of the data from which learning is faster and just as effective?
          - Finding prototypes can be as easy as "cluster and take just a few
            from each cluster"
          - But there are [many other
            methods](https://www.researchgate.net/profile/Jose_Francisco_Martinez-Trinidad/publication/220637923_A_review_of_instance_selection_methods/links/0912f50c21a20bd92b000000.pdf)
    - eg. apply a data miner to an optimizer to divide up the data to make the
      whole process much faster?
See [500+ faster than deep learning](https://arxiv.org/pdf/1802.05319.pdf). 
- Does that method need additional support to enable explanation of their output?
- Do their models fail the stability test? 
    - How does that  method respond if you run it N times on 90% of the data? 
    - And if they do, can you find regions of the data where the performance is stable?
- How to reduce the CPU and RAM and runtime requirements
of that method by large amounts e.g. 
see [500+ faster than deep learning](https://arxiv.org/pdf/1802.05319.pdf). 
- If we stream over the data, how soon does this model stabilize? 
- If we inject mutations into the data, can
this method be used to recognize that strange data? Once the wierd data
arrives, how long (if ever) before the model recovers? 
- If a model is update, can be it done some _minimally_; i.e. with least change to the existing model?


Why these 

report when the baseline is not enough (e.g. see One1 being used as
preferomfnac epredictor for other, more complex learners)

XXXX why [simplicity](simplicity.md).


XXX what does [explanatory](explaination.md) mean

XXX streaming

XXX revising

re stochasthic. Disagree
stochastic = scalability, stability (shout stochastic you won't know
if your re living in some some tiny  island surrounded by forces of
chaos)

- In some software engineering applications, solution robustness may
be as im- portant as solution functionality. For example, it may be
better to locate an area of the search space that is rich in fit
solutions, rather than identifying an even better solution that is
surrounded by a set of far less fit solutions.

- Hitherto, research on SBSE has tended to focus on the production of
the fittest possible results. However, many application areas require
solutions in a search space that may be subject to change. This makes
robustness a natural second order property to which the research
community could and should turn its at- tention [30].

M. Harman and B. Jones. Search-based software engineering. Journal of
Information and Software Technology, 43:833–839, December 2001.

## All Connected

The more we compress the smaller the memory and the faster we learn and the less we need to share (so
more privacy).

The more we understand the data's prototypes the more we know what is usual/
unusual so we more we know what is anomlaous so the easier it is to ofer a
certification envelope

Note that if our compression method is somehow hierarhical and if we track the
errors seen by our learners in different subtrees then the more we know which
parts of the model need revising (and which can stay the same). Which means we
only make revisions to the parts that matter, elaving the rest stable.


## Other Requirements

### No eval tools 

Tests conclusion stability

- across mulitple data sets (if
  avaialable) 
- or across multiple subsets of know scenarios

See [Evalaution](eval) for many examples of that kind of evaluation.

- Note that these can significantly increase the computational cost of using learners. 
- Hence, the need to [faster](faster), [lighter](lighter) AI algorithms. 

## No support for stats tests

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

