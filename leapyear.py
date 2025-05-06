year=int(input('enter the year'))
if (year%4==0 and year%100!=0)or(year%400==0):
    print("is a leap year")
else:
    print('not a leap year') 
x=year%4
if x!=0:
    print('previous year',year-4)
else:
    print('next year',year+4)