# help encode chinese
#-*- coding: utf-8 -*-

# import math for mathExercise
import math

# leap year calc
def isLeapYear(year):
  "return true if input is leap year, otherwise false"
  if ( (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0) ):
    return 1
  else:
    return 0 

# math calc
def mathExercise():
  "some exercises on math operators and methods"
  print "-- result of 12*34+78−132/6 is " + str( 12*34 + 78 - (132/6)  )
  print "-- result of (12*(34+78)−132)/6 is " + str( (12 * (34 + 78) - 132)/6 )
  print "-- result of (86/40)**5 is " + str((86/40)**5)

  print "-- result of 145%23 is " + str( 145 % 23 )

  print "-- result of sin(0.5) is " + str( math.sin(0.5) )
  print "-- result of cos(0.5) is " + str( math.cos(0.5) )

  return

from math import sqrt

# calc prime numbers under num
def listPrimes(num):
  "list all prime numbers under num"
  re = []
  for n in range(2, num):
    flag = True
    for sn in range(2, int(sqrt(num)) + 1):
      if n % sn == 0:
	flag = False
	break
    if flag:
      re.append(n)

  print re

  return

print isLeapYear(2001)
print isLeapYear(2008)

mathExercise()

listPrimes(10)
