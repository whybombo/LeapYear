import calendar

year = int(input("Enter the Year to check for a Leap Year: "))

result = calendar.isleap(year)

if ( result ):
    print("{0} is a Leap Year".format(year))
else:
    print("{0} is not a Leap Year".format(year))