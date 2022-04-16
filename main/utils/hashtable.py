import os
from utils.functions import initDirectory, createJsonFile, loadDataFromJson, saveDataToJson

class HashTable:

	# Create empty bucket list of given size
	def __init__(self, size):
		print('hash class instance')
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		print('hash create', self.size)
		os.chdir('../')
		current_directory = os.getcwd()
		initDirectory(current_directory)
		print('current_directory', current_directory)
		os.chdir('./data/')
		print('os.getcwd()',os.getcwd())
		current_directory = os.getcwd()
		print('current_directory final', current_directory)
		# Create a new directory for the data
		for i in range(self.size):
			print('nodo', i +1)
			os.mkdir(current_directory + '/nodo' + str(i+1))
			createJsonFile(current_directory + '/nodo' + str(i+1), 'base.json',[])
		# Create a json file on the data directory
		return [[] for _ in range(self.size)]

	# Insert values into hash map
	def set_val(self, key, val):
		# Get the index from the key
		# using hash function
		hashed_key = hash(key) % self.size
		print('hashed_key', hashed_key)
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]
		print('bucket', bucket)
		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be inserted
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key to be inserted,
		# Update the key value
		# Otherwise append the new key-value pair to the bucket
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	# Return searched value with specific key
	def get_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key being searched
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key being searched,
		# Return the value found
		# Otherwise indicate there was no record found
		if found_key:
			return record_val
		else:
			return "No record found"

	# Remove a value with specific key
	def delete_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be deleted
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	# To print the items of hash map
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)


#hash_table = HashTable(50)

# insert some values
#hash_table.set_val('gfg@example.com', 'some value')
#print(hash_table)
#print()

#hash_table.set_val('portal@example.com', 'some other value')
#print(hash_table)
#print()

# search/access a record with key
#print(hash_table.get_val('portal@example.com'))
#print()

# delete or remove a value
#hash_table.delete_val('portal@example.com')
#print(hash_table)