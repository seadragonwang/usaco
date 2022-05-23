"""
ID: wang.se1
LANG: PYTHON3
TASK: friday
"""
def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 != 0:
			return False
		return True

def calculate_days_in_a_month(year, month):
	if month == 2:
		if is_leap_year(year):
			return 29
		else:
			return 28
	elif month in (1,3,5,7,8,10,12):
		return 31
	else:
		return 30

def calculate_week_day(year, month , day, frequencies):
	num_of_days = 0
	for y in range(1900, year):
		if is_leap_year(y):
			num_of_days += 366
		else:
			num_of_days += 365
	for m in range(1, month):
		num_of_days += calculate_days_in_a_month(year, m)

	num_of_days += day
	frequencies[num_of_days % 7] += 1

def calculate_week_frequency(years, frequecies):
	for y in range(1900, 1900+years):
		for m in range(1, 13):
			calculate_week_day(y, m, 13, frequecies)

if __name__ == '__main__':
	frequencies = {1:  0, 2:  0, 3:  0, 4:  0, 5:  0, 6:  0, 0:  0, }
	keys = [6, 0, 1, 2, 3, 4, 5]
	with open("friday.in", "r") as fin:
		years = int(fin.readline().strip())
		calculate_week_frequency(years, frequencies)
		with open("friday.out", "w") as fout:
			first = True
			for key in keys:
				if first:
					fout.write(f"{frequencies[key]}")
					first = False
				else:
					fout.write(f" {frequencies[key]}")

			fout.write("\n")