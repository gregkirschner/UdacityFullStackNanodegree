""" 
Removing all numbers from file names in the current working directory by utilizing
Regular Expressions.

This version utilizes Regular Expressions and re.sub().
The prior version checked for ASCII characters.
"""

import os, re


def rename_file():
  #List current working directory and its files
  cwd = os.getcwd()
  print "Current working directory: {}".format(cwd)
  print ("Original Directory: \n")
  print os.listdir(cwd)

  #Rename each file
  for each_file in os.listdir(cwd):
      os.rename(each_file, re.sub('[0-9]', '',each_file))
  print ("\nChanged Directory: \n")
  print os.listdir(cwd)
