import random

def read_words(filename):
	file = open(filename, 'r')
	words = []
	for word in file:
		words.append(word.strip())
	return words

nouns = read_words("./nouns.txt")
adjs  = read_words("./adjectives.txt")

def generate():
	noun = random.choice(nouns)
	adj  = random.choice(adjs)

	noun = noun[0].upper() + noun[1:-1] + noun[-1].upper()
	adj  = adj[0].upper() + adj[1:-1] + adj[-1].upper()

	passwd = adj + "-" + noun
	# passwd = passwd.replace("for", "4")
	# passwd = passwd.replace("too", "2")
	# passwd = passwd.replace("to", "2")
	# passwd = passwd.replace("l", "1")
	# passwd = passwd.replace("b", "6")
	# passwd = passwd.replace("o", "0")

	# tmp = passwd.split('-')
	# tmp = tmp[0] + tmp[1]

	# if tmp.isalpha():
	passwd += "-" + str(len(passwd) - 1)

	return passwd