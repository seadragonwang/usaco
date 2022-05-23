"""
ID: wang.se1
LANG: PYTHON3
TASK: ride
"""
def calculate_product(name):
	product = 1
	for c in name:
		product *= ord(c) - 64
	return product

def ride(comet_name, group_name):
	product_comet = calculate_product(comet_name)
	product_group = calculate_product(group_name)
	if product_comet % 47 == product_group % 47:
		return "GO"
	else:
		return "STAY"


if __name__ == '__main__':
	with open("ride.in", "r") as fin:
		comet_name = fin.readline()
		group_name = fin.readline()
		with open("ride.out", "w") as fout:
	 		fout.write(ride(comet_name, group_name) + "\n")