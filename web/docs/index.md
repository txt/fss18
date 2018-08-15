<img src="img/ncstate.png" align=right width=300><br clear=right>
<img src="http://ai4se.net/img/ncsu-logo.png" align=right width=100>
# Foundations of Software Science

Fall 2018

## Why This Subject

Q: So what is current "not" SE, but soon must be?    
A: AI

Don't believe me? Well here is a pressing question;

- As society uses more AI, SE folks will be required to us and maintain and extend that software
- So what are the "bad smells" of an AI system that would movitate reorganizing that code?

Enter this subject.


## Software Engineering: the past

SE's past is full of cases where

- someone declared "X" was not part of SE
- then we ignored them and added "X" to SE
- and lots of things got lots better

e.g.  From [Boehm, Keynote, 2004](http://ase-conferences.org/ase/past/ase2004/download/KeynoteBoehm.pdf), slide 8:

- "The notion of 'user' cannot be precisely defined, and therefore has no place in CS or SE." 
       - Edsger Dijkstra, ICSE 4, 1979
- "Analysis and allocation of the system requirements is not the responsibility of the SE group but is a prerequisite for their work." 
       - Mark Paulk at al., SEI Software CMM\* v.1.1, 1993

e.g. Harlin Mills, 1984: software engineers shoul write, but not run or test, their own software

- aaa

## Software Engineering: the future

From [Software
Analytics:
What’s Next?](http://menzies.us/pdf/18analytics.pdf), IEEE Software, Sept/Oct 2018:

- "Consider the rise of the data scientist in industry. 
     - Many organizations now pay handsomely to hire large teams of data scientists. 
     - For example, at the time of this writing, there are more than 1,000 Microsoft employees exploring project data using software analytics. 
     - These teams are performing tasks that a decade ago would have been called cutting-edge research. 
     - But now we call that work _standard operating procedure_."
- "Every innovation also offers new opportunities. 
     - There is a flow-on effect from software analytics to other AI tasks outside of software engineering. 
     - Software analytics lets software engineers learn about AI techniques, all the while practicing on domains they understand (i.e., their own development practices). 
     - Once developers can apply
data-mining algorithms to their data, they can build and ship innovative AI tools. 
     - While sometimes those tools solve software engineering problems (e.g., recommending what to change in source code), they can also be used on a wider range of problems. 
     - That is, we see software analytics as the training ground for the next generation of AI-literate software engineers working on applications such as image recognition, large-scale text mining, autonomous cars,  drones,
     etc."


## Softwre Engineering: the past

For full documentation visit [mkdocs.org](https://mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

```lua
local function a(x,y)
  return 2+a -- 
end
```
