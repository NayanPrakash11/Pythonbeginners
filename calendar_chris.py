import calendar
""" trying out the calendar"""

#sep=calendar.TextCalendar(calendar.MONDAY)
#sep.prmonth(2019, 3)
#print(sep)
#year=int(input("Enter the year to display: "))
#print(calendar.prcal(year))

cal=open("/Users/chris/pygit/cal.html", "w")
c=calendar.HTMLCalendar(calendar.MONDAY)
cal.write(c.formatyear(2019))
cal.close()

