# Homework Week1, Week2

"""

## Todo

1. Create a public Github repo (NOT in NC State Github, but in the other one) 
2. Add "timm" as a team member to that repo. How? 
     - go the repo's organization's settings
     - on left-hand-side menu go to Collaberators and teams
     - then Enter "timm" under "Collaborators".
3. Start a file with the following header (containing `class O`).
4. For Week1, address the _Python101_ task.
5. For Week2, address the _Table reader_ task.

Commit the code (w1.py, w2.py) and a transcript of the output (called w1.txt,
w2.txt) to a sub-directory in your repo called `w12`. 

Paste  a link to that directory in the commit sheet.

## A Simple Unit Test Rig (in Python)

"""
import re,traceback

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f
"""

### Test rig, in action

- Functions are called
as a side-effect of load the file.
- The function comment is something
the above rig prints out. 
- If assertions fail, it prints
the error but keeps on going to run the other tests.

"""
@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1

if __name__== "__main__":
  O.report()
"""

For example, if you load this file with

     python3 thisfile.py

you will see

    -----| testingFailure |-----------------------
    # this one must fail.. just to
    # test if the  unit test system is working
    Traceback (most recent call last):
      File "w1.py", line 29, in k
        f()
      File "w1.py", line 52, in testingFailure
        assert 1==2
    AssertionError

    -----| testingSuccess |-----------------------
    # if this one fails, we have a problem!
    # pass

    # pass= 1 fail= 1 %pass = 50%

Note the last line (number of passes and failes in the code).

## Task1 (week1): Python101

- Read [Basic Python](../pdf/python201.pdf) 
- Write 27 functions like `testingSuccess` (above)
that demonstrate you understand that the code on pages 5 to 33, skipping p21 (so one function
for one thing on each page).


## Task2 (week2): Sample Table Data (that we want to read)

Suppose we need to read in a table.

"""
DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""
"""

Then we need to learn the type of the data (on row1) which in this case is

- numeric (if name has "_$_");
- ignrore this column (if name has "_>_");
-  string, otherwise.

And some tables of data are more challenging that others. Here's one where

- there are comments (after a "_#_");
- rows can continue onto the next line (if they end in ",");
- there can be blank lines in the file

"""
DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,
        
                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""
"""
Regardless of those details, when we read both these strings, we see as output

     ['outlook', '$temp', 'windy', 'play']
     ['sunny', 85.0, 'FALSE', 'no']
     ['sunny', 80.0, 'TRUE', 'no']
     ['overcast', 83.0, 'FALSE', 'yes']
     ['rainy', 70.0, 'FALSE', 'yes']
     ['rainy', 68.0, 'FALSE', 'yes']
     ['rainy', 65.0, 'TRUE', 'no']
     ['overcast', 64.0, 'TRUE', 'yes']
     ['sunny', 72.0, 'FALSE', 'no']
     ['sunny', 69.0, 'FALSE', 'yes']
     ['rainy', 75.0, 'FALSE', 'yes']
     ['sunny', 75.0, 'TRUE', 'yes']
     ['overcast', 100.0, '90', 'TRUE']
     ['overcast', 81.0, 'FALSE', 'yes']
     ['rainy', 71.0, 'TRUE', 'no']

### Functions

The following functions implement the table reader.

"""
def lines(s):
  "Return contents, one line at a time."
  yourCodeHere()

def rows(src):
  """Kill bad characters. If line ends in ',' 
   then join to next. Skip blank lines."""
  yourCodeHere()


def cols(src):
  """ If a column name on row1 contains '?', 
  then skip over that column."""
  yourCodeHere()


def prep(src):
  """ If a column name on row1 contains '$', 
  coerce strings in that column to a float."""
  yourCodeHere()
"""

### Test cases

"""
def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)
