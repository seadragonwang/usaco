"""
ID: wang.se1
LANG: PYTHON3
TASK: blist
"""
if __name__ == '__main__':
	with open("blist.in", "r") as fin:
		ncows = int(fin.readline().strip())
		s = []
		t = []
		b = []
		for i in range(ncows):
			fields = fin.readline().strip().split(" ")
			s.append(int(fields[0].strip()))
			t.append(int(fields[1].strip()))
			b.append(int(fields[2].strip()))
		times = sorted(s + t)
		max_buckets = 0
		for time in times:
			nbuckets = 0
			for i in range(ncows):
				if s[i] <= time <= t[i]:
					nbuckets += b[i]
			if nbuckets > max_buckets:
				max_buckets = nbuckets

		with open("blist.out", "w") as fout:
			fout.write(f"{max_buckets}\n")