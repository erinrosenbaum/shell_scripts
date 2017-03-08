# Erin Rosenbaum
# March 10, 2017
# cs_344 winter_2017
# mypython.py

import random
import string
from random import randint

# create 3 files with write permissions.
f1 = open("file1", "w")
f2 = open("file2", "w")
f3 = open("file3", "w")

my_files = [f1, f2, f3]

for file in my_files:
  random_string = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
  file.write(random_string)
  file.write('\n')
  print random_string
  file.close()

rand_int1 = randint(1, 42)
rand_int2 = randint(1, 42)
print rand_int1
print rand_int2
print rand_int1 * rand_int2


