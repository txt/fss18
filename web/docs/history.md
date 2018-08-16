

#  SE + AI: then and now


<img src="https://i.pinimg.com/originals/2f/47/ba/2f47ba12ad4d7d8282fe68e67911a830.png" width=700">

SE's past is full of cases where

- someone declared "X" was not part of SE
- then we ignored them and added "X" to SE
- and lots of things got lots better

So the question I pose to you is this:

Q: What is currently "not" SE, but soon must be?    
A: AI

Enter this subject


## SE: the past

### e.g. "SE is not about requirements engineering" (which is wrong)

e.g.  From [Boehm, Keynote, 2004](http://ase-conferences.org/ase/past/ase2004/download/KeynoteBoehm.pdf), slide 8:

- "The notion of 'user' cannot be precisely defined, and therefore has no place in CS or SE." 
       - Edsger Dijkstra, ICSE 4, 1979
- "Analysis and allocation of the system requirements is not the responsibility of the SE group but is a prerequisite for their work." 
       - Mark Paulk at al., SEI Software CMM\* v.1.1, 1993

### e.g. "Programmning  is not about testing" (wrong again)

e.g. [Harlin Mills, 1984](https://pdfs.semanticscholar.org/9141/281be67750c291d12f4ddf92417aaa6625f6.pdf)
: software engineers should write, but not run or test, their own software

- "Cleanroom software engineering"
- No unit testing (instead, mathematical verification)
     - so before we run anything, we write perfect code
- And there is a seperate testing team to the programming team

### e.g. "Programming  is not about deploying software"  (so very, very wrong)

- Before devops, the coding team used to hand off the system to the production team
- Now we do much less of that.. achieving must faster change cycles

### Q: So What's next?

A: AI

## SE: the present

Software now mediates what we see and how we act

- Chemists win  Nobel Prize for  [software sims](http://goo.gl/Lwensc)
- Engineers use software to design [optical tweezers, radiation therapy, remote sensing,  chip design](http://goo.gl/qBMyIZ)
- Web analysts use software  to analyze clickstreams to [improve sales and marketing strategies](http://goo.gl/b26CfY)
- Stock traders write software to [simulate trading strategies](http://www.quantopian.com)
- Analysts write software  to mine   labor statistics data to [review proposed gov policies](http://goo.gl/X4kgnc)
- Journalists use software   to analyze economic data, [make visualizations of their news stories](http://fivethirtyeight.com)
- Etc etc etc

In short, now more than ever, software really really matters

- In London or New York,
     - The time for ambulance to reach patient
[is controlled by models](http://goo.gl/8SMd1p)
- If you cross the border Arizona to Mexico,
     - Models determine if you are taken
away for extra security measures
- If you default on a car loans,
     - Models determine when (or if)
someone repossesses your car
- Autonomous cars
- Software is essential to international financial and transport systems; our energy generation and distribution systems; and even the pacemakers that control the beat of our hearts.
- Looking forward,  to the forthcoming age of autonomous cars and
flying drones, it is clear that software models (written in traditional
programming languages or in some next-generation interpretation)
will be key in determining what we can do, when, where, and how.


So how can we help our AI systems reason better about our data, and our models?

- Using data mining,
we might learn a model from data that predicts for (say) a single target class;
- Using optionzers, we might  a multi-objective optimizer to find what solutions score best on multiple target variables.
- Also, data miners can be used to
to summarize the data, after which optimizers can [leap to better solutions, faster](http://menzies.us/pdf/15gale.pdf);
- Also, optimizers can be used to [select intelligent settings for data mining algorithms](https://arxiv.org/pdf/1609.01759.pdf) e.g. such as how many trees should be included in a random forest.


## SE: the future

Software enginenering isn't just about software any more

-  Olde SE: just polish up the lens of the telescope
-  New SE (with AI): use the telescope to look and understand and change "things"


After "continuous integration" (where we automated everything)

- Comes "AI everywhere" (where we automate automation).


From [Software
Analytics:
What’s Next?](http://menzies.us/pdf/18analytics.pdf), IEEE Software, Sept/Oct 2018:

"Consider the rise of the data scientist in industry. 

- Many organizations now pay handsomely to hire large teams of data scientists. 
- For example, at the time of this writing, there are more than 1,000 Microsoft employees exploring project data using software analytics. 
- These teams are performing tasks that a decade ago would have been called cutting-edge research. 
- But now we call that work _standard operating procedure_."


"Every innovation also offers new opportunities. 

- There is a flow-on effect from software analytics to other AI tasks outside of software engineering. 
- Software analytics lets software engineers learn about AI techniques, all the while practicing on domains they understand (i.e., their own development practices). 
- Once developers can apply
data-mining algorithms to their data, they can build and ship innovative AI tools. 
- While sometimes those tools solve software engineering problems (e.g., recommending what to change in source code), they can also be used on a wider range of problems. 
- That is, we see software analytics as the training ground for the next generation of AI-literate software engineers working on applications such as image recognition, large-scale text mining, autonomous cars,  drones,
     etc."

"What is the most
important technology newcomers should learn to make themselves better at data science (in general) and software analytics (in particular)? 

- "To answer this question, we need a workable definition of “science,” which we take to mean a community of people collecting, curating, and critiquing a set of ideas. 
    - In this community, everyone does each other the courtesy to try to prove this shared pool of ideas.
- By this definition, most data science (and much software analytics) is not science. 
    - Many developers use software analytics tools to produce conclusions, and that’s the end of the story. 
    - Those conclusions are not registered and monitored. 
    - There is nothing that checks whether old conclusions are now out of date (e.g., using anomaly detectors). 
    - There are no incremental revisions that seek minimal changes when updating old ideas.

<center>
<img  src="https://raw.githubusercontent.com/txt/fss16/master/img/science.png">
</center>

"If software analytics really wants to be called a science, then it needs to be more than just a way to make conclusions about the present. 

- Any scientist will tell you that all ideas should be checked, rechecked, and incrementally revised. 
- Data science methods such as software analytics should be a tool for assisting in complex discussions about ongoing issues.
- Which is a long-winded way of saying that the technology we most need to better understand software analytics and data science is ... science."


