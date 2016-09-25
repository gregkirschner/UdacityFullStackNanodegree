""" 
Removing all characters from file names in the current working directory
that are not one of the following:
  1. letters
  2. periods (.)
  3. underscores (_)

This file utilizes ASCII character values to determine what to keep and
remove from the file names.
"""

import os

#ASCII Table  #65 to 90 are capital letters
#             #97 to 122 are lowercase letters
#             #46 is period:  .
#             #95 is underscore:  _


def rename_file():
  #List current working directory and its files
  cwd = os.getcwd()
  print "Current working directory: {}".format(cwd)
  print ("Original Directory: \n")
  print os.listdir(cwd)

  #Rename each file
  for each_file in os.listdir(cwd):
      new_file_name = ''
      for letter in each_file:
        if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122) or (
          ord(letter) == 46) or (ord(letter) == 95):
          new_file_name += letter
        else:
          continue
      os.rename(each_file, new_file_name)

  print ("\nChanged Directory: \n")
  print os.listdir(cwd)

