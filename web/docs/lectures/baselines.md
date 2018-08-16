# Baseline for an "Adequate" AI

## What do uou want?

Requirements of a Baseline Estimation Model. Extended from [Sarro, TOSEM'18](http://www0.cs.ucl.ac.uk/staff/F.Sarro/resource/papers/SarroTOSEM18.pdf):

- Be simple to describe, implement, and interpret.
- Be deterministic in its outcomes.
- Be applicable to mixed qualitative and quantitative data.
- Offer some explanatory information regarding the prediction
  by representing generalised properties of the underlying data.
- Have no parameters within the modelling process that require tuning. Be publicly available via a reference implementation and associated environment for execution.
- Generally be more accurate than a random guess or an estimate based purely on the distribution of the response variable.
- Be robust to different data splits and validation methods.
- Do not be expensive to apply.
-  Offer comparable performance to standard methods.


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

## Other Requirements

### No eval tools 

Tests conclusion stability

- across mulitple data sets (if
  avaialable) 
- or across multiple subsets of know scenarios

See [Evalaution](eval) for many examples of that kind of evaluation.

- Note that these can significantly increase the computational cost of using learners. 
- Hence, the need to [faster](faster), [lighter](lighter) AI algorithms. 

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

