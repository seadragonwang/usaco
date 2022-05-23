"""
ID: wang.se1
LANG: PYTHON3
TASK: beads
"""


def get_beads_around_white(beads, index):
	if beads[index] != 'w':
		return None
	if index == 0:
		j = index
		while j + 1 < len(beads) and beads[j + 1] == 'w':
			j += 1

		after = beads[j + 1]
		return None, None, after, j+1
	if index == len(beads) - 1:
		i = index
		while i - 1 >= 0 and beads[i - 1] == 'w':
			i -= 1
		before = beads[i - 1]

		return before, i-1, None, None
	j = index
	while j + 1 < len(beads) and beads[j + 1] == 'w':
		j += 1

	after = beads[j + 1]
	i = index
	while i - 1 >= 0 and beads[i - 1] == 'w':
		i -= 1
	before = beads[i - 1]

	return before, i-1, after, j+1


def replace_nonspecial_beads(beads):
	i = 0
	while i < len(beads):
		if beads[i] == 'w':
			before, before_pos, after, after_pos = get_beads_around_white(beads, i)
			if not before:
				beads[i:after_pos] = after*(after_pos-i)
			elif not after:
				beads[before_pos+1:i] = before*(i-before_pos-1)
				break
			elif after == before:
				beads[before_pos+1:after_pos] = before*(after_pos-before_pos-1)
			i = after_pos + 1
		else:
			i += 1
	return beads


def generate_beads(beads):
	for i in range(len(beads)):
		if beads[i] == 'w':
			before, before_pos, after, after_pos = get_beads_around_white(beads, i)
			if before != after:
				if i > 0:
					if i+1 < len(beads):
						beads = beads[:i] + before + beads[i+1:]
					else:
						beads = beads[:i] + before
				else:
					if i+1 < len(beads):
						beads = before + beads[i+1:]
					else:
						beads = before
	return beads


if __name__ == '__main__':
	with open("beads.in", "r") as fin:
		num_of_beads = int(fin.readline().strip())
		beads = fin.readline().strip()
		beads = list(beads)
		result = []
		replace_nonspecial_beads(beads)

		num_of_same_beads = 1
		for i in range(1, len(beads)):
			if beads[i] == beads[i-1]:
				num_of_same_beads += 1
			else:
				result.append(num_of_same_beads)
				num_of_same_beads = 1

		result.append(num_of_same_beads)
		print(result)
	# final_result = None
	# for i in range(1, len(result)):
	# 	if final_result:
	# 		if result[i]+result[i-1] > final_result:
	# 			final_result = result[i]+result[i-1]
	# 	else:
	# 		final_result = result[i]+result[i-1]
	# if result[-1] + result[0] > final_result:
	# 	final_result = result[-1] + result[0]
	# with open("beads.out", "w") as fout:
	# 	fout.write(f"{final_result}\n")
