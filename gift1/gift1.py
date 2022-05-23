"""
ID: wang.se1
LANG: PYTHON3
TASK: gift1
"""
def read_inputs_for_members(members, fin):
	line = fin.readline().strip()
	while line:
		member_obj = members[line]
		fields = fin.readline().strip().split(" ")
		member_obj["initial_value"] = int(fields[0].strip())
		member_obj['value'] = -member_obj["initial_value"]
		num_of_recipients = int(fields[1].strip())
		recipients = []
		for i in range(num_of_recipients):
			recipients.append(fin.readline().strip())
		member_obj["recipients"] = recipients
		line = fin.readline().strip()

def calculate_gift(members):
	for key in members.keys():
		member = members[key]
		if len(member["recipients"]):
			amount_give = int(member["initial_value"] / len(member["recipients"]))
		else:
			amount_give = 0
		for recipient in member["recipients"]:
			member_obj = members[recipient]
			member_obj["value"] += amount_give
		member["value"] += member["initial_value"] - amount_give * len(member["recipients"])

if __name__ == '__main__':
	with open("gift1.in", "r") as fin:
		np = int(fin.readline().strip())
		members = {}
		for i in range(np):
			member_name = fin.readline().strip()
			members[member_name] = {"name": member_name}
		read_inputs_for_members(members, fin)
		calculate_gift(members)
		with open("gift1.out", "w") as fout:
			for key in members.keys():
	 			fout.write(f"{key} {members[key]['value']}\n")