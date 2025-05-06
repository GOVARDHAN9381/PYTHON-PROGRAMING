# Input year
year = int(input("Enter Date: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Given year is Leap Year")
else:
    print("Given year is Non Leap Year")
    prev_year = year - 1
    while not ((prev_year % 400 == 0) or (prev_year % 4 == 0 and prev_year % 100 != 0)):
        prev_year -= 1
    print("Leap Year:", prev_year)
