#To check if a year is a leap year or not
Leap = lambda year :year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
