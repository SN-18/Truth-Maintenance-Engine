## Truth Maintenance Engine
A Truth Maintenance System is a knowledge representation for maintaining beliefs and their dependencies. A truth maintenance system updates its knowledge base and maintains consistency through revision. 


## Files

1. main.py: Contains the driver code
2. propositional.py : Contains the Propositional logic to maintain the TMS, the TMS class and the Knowledge Base
3. logic.txt: Contains a series of assertions int the following form:

-1 ASSERT (a)

This statements updates the KB with the truth of statement a. Similarly, 

-2 RETRACT(1)

This statement is meant to update the KB by retracting statement 1. Doing this would also impact the statements that contain statment 1 as a truth, such as a^b (where ^ represents conjunction). This in turn would need to update the KB by removing statements that contain a^b, and so on, for it's dependents.


## How to run

1.Check your python version by opening up a terminal environment (terminal on mac OS X, cmd on windows, etc) and using <br>
$ python --version

This should generate something like this, if python is installed on the system.

<img width="427" alt="image" src="https://user-images.githubusercontent.com/83748468/208569830-55cc116b-e93e-4840-b780-e143e7d68074.png">

2. If Python is not installed, use a package manager like pip and commands such as:<br> 
$ pip install python

Visit:[Python's Official Download Page](https://www.python.org/downloads/) for information on how to download and install python.

3. cd to your directory that contains the project. (cd command is short for change directory, read [cd](https://man7.org/linux/man-pages/man1/cd.1p.html), for example, for the TMS folder on user's desktop:<br>
$cd .~/Desktop/TMS

4.Run the command python main.py from any python environment or terminal in IDE,<br>
$ python main.py

This would invoke the driver code. This would in turn call all the associated files and update the KB, as per incoming knowledge or beliefs from the logic.txt file.









