# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []

def add_to_index(index,keyword,url):
	for e in index:
		if e[0] == keyword:
			e[1].append(url)
			return
	index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	for e in content.split():
		add_to_index(index,e,url)


add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


