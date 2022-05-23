"""
ID: wang.se1
LANG: PYTHON3
TASK: mixmilk
"""
if __name__ == '__main__':
	with open("mixmilk.in", "r") as fin:
		line = fin.readline().strip()
		capacities = []
		amounts = []
		while line:
			c, a = line.split(" ")
			capacities.append(int(c.strip()))
			amounts.append(int(a.strip()))
			line = fin.readline()
	b = []
	i = 1
	while i < 101:
		start = (i + 2) % 3
		end = i % 3
		if amounts[start] + amounts[end] > capacities[end]:
			amounts[start] = amounts[start] + amounts[end] - capacities[end]
			amounts[end] = capacities[end]
		else:
			amounts[end] = amounts[start] + amounts[end]
			amounts[start] = 0
		i += 1

	with open("mixmilk.out", "w") as fout:
		for i in range(len(amounts)):
			fout.write(f"{amounts[i]}\n")
