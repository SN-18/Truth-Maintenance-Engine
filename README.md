# CSC 520 AI (Fall 22)
# Assignment 4 (Question 2)

# @Author: Saurabh Nanda
# @Unity: snanda2@ncsu.edu

# Files
'''
1.)main.py
2.)propositional.py
'''

# How to run
'''
1.) Make sure to install python 3.X by either pip install python or using a package manager like homebrew or
yum, etc
2.) Run the command python main.py from any python environment or terminal in IDE


# main.py
'''Contains driver code. Invoking main.py runs the project.'''

# propositional.py
'''Contains src code. It contains the class TMS, short for Truth Maintenance System,
 and implements the following class methods (can be invoked by declaring t.assert(...),t.retract(...)
 and t.resolution(...), where ... denotes respective arguments:

# logic.txt
'''Contains the propositional logic statements in the form of conjuncts, (a, b) for example,
 means (a or b) and ~a is same as (not a), in this context '''

1.) assert_s(): On encountering an ASSERT from logic.txt, it updates the KB. assert_s stands for
assert statement (naming logic: since assert is a keyword in python). Prints the justification
for statement added after updating kb.
2.) retract_s(): On encountering a retract from logic.txt, it recursively retracts the statement mentioned,
and it's dependencies, if any. Prints the justification of a statement being removed from KB.
3.) resolution(): Encountering like (a or b) and (~a) would resolve to b, and three statements would be
added to the KB.




