# EXERCISE 1: Software versions and dependencies

#1.1 What version of your language (Python/R) are you running?
import sys
print(sys.version)

#1.2 What version of pandas (Python) or dplyr (R) do you have installed?
import pandas as pd
print(pd.__version__)

#1.3 What other packages do you use for your analysis?
# In terminal: pip list

#1.4 Pick one package from your list — what are its dependencies?
# In terminal: pip show pandas