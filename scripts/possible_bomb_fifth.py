import string

array_123 = "isrveawhobpnutfg"
possibilities = {"g": [], "i": [], "a": [], "n": [], "t": [], "s": []}
def get_index(index : str):
	return array_123[ord(index) & 15]

strings = string.ascii_lowercase + string.ascii_uppercase + string.digits

for i in strings:
	index = get_index(i)
	if index in possibilities.keys():
		possibilities[index].append(i)

for i in possibilities.keys():
	print(f"{i}: {possibilities[i]}")

for g in possibilities["g"]:
	for i in possibilities["i"]:
		for a in possibilities["a"]:
			for n in possibilities["n"]:
				for t in possibilities["t"]:
					for s in possibilities["s"]:
						print(f"{g}{i}{a}{n}{t}{s}", end=" ")
