# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
	table = []
	n = 0
	while n < nbuckets:
		table.append([])
		n += 1
	return table

print make_hashtable(8)

def make_hash_table(nbuckets):
	table = []
	for unused in range(0,nbuckets):
		table.append([])
	return table

print make_hashtable(8)