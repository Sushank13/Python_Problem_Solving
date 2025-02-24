# a leap year is the one that is evenly divisible by 4 but not 100 OR is evenly divisible by 400
# ex: year 1992 divisble by 4 but not 100, therefore, is a leap year
year=int(input())
def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False