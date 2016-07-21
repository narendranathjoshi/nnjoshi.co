from collections import defaultdict
import pickle

# Read the cities text file
cities = open("cities.txt").read()
cities = map(lambda x: x.strip(), cities.split("\n"))

# build a prefix tree from the cities
tree = defaultdict(list)

for city in cities:
	for i in range(1, len(city)):
		tree[city[:i].lower()].append(city.lower())

# serialize and dump the index to a file
pickle.dump(tree, open("index.pickle", "w"))

def search(q):
	return tree[q.lower()]

print search("al")