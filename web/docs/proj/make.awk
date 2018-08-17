BEGIN {N=C=0}
gsub(/^\"\"\"/,"") { 
     C=1-C
     if (N) print C ? "```" : "```python"; 
     N=1
     next
     }
     {print} 

     END {if (!C) print "```"}
