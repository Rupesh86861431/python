month = input("Enter month : ")
day = int(input("Enter no.of days: "))

if month in ('january','february','march'):
	season = 'winter'
elif month in ('april','may','june'):
	season = 'summer'
elif month in ('july','august','september'):
	season = 'spring'
else:
	season = 'autumn'

if (month == 'march') and (day > 19):
	season = 'summer'
elif (month == 'june') and (day > 20):
	season = 'spring'
elif (month == 'december') and (day > 20):
	season = 'winter'
print("Season is",season)
