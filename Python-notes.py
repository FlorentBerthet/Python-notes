

# Functions - args and kwargs

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'bio', name='John', age=22)

	# ('math', 'bio')
	# {'age': 22, 'name': 'John'}



# Functions - Return number of days in that month in that year

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""return true for leap years"""
	return year % 4 == 0 and (year %100 != 0 or year %400 == 0)

def days_in_month (year, month):
	"""Return number of days in that month in that year"""
	if not 1 <= month <=12:
		return 'Invalid month'
	if month == 2 and is_leap(year):
			return 29
	return month_days[month]

print(is_leap(2020))
print(days_in_month(2019, 2))
