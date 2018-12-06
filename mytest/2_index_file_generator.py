import re
import unicodedata
import codecs
import locale

def sort_locale(mylist):
	# sort mylist as Hungarian alphabet
	locale.setlocale(locale.LC_ALL, "hu_HU.utf8")
	mylist.sort(key=locale.strxfrm)
	return mylist

def read_ascii_file(file):
	# open file and encode as utf-8
	file = codecs.open(file,'r',encoding='UTF-8',errors='ignore')
	data = file.read()

	# convert data rows to list
	rows = data.replace('\r','').split('\n')

	# join rows and list distinct list of words by Hungarian alphabet
	words = ' '.join(rows)
	words = re.findall(r'\w+',words)
	words = sort_locale(list(set(words)))

	# collect each word to my_data dictionary with their row indexes
	my_data = {}
	for word in words:
		index = []
		if word.lower() not in my_data.keys():
			for j in range(0,len(rows)):
				if word.lower() in rows[j].lower():
					index.append(str(int(j)+1))
					my_data.update({word:index})

	# format text output
	text = ''
	for key in my_data.keys():
		text=text+key+' '+','.join(my_data[key])+'\n'
	return text

def write_file(text, file_index):
	# write text to file_index
	file = open(file_index, 'w')
	file.write(text)
	file.close()

########################################################

if __name__ == "__main__":
	text = read_ascii_file('szoveg.txt')
	write_file(text, 'szoveg-index.txt')
