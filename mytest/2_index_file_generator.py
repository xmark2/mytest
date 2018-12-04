import re
import unicodedata
import codecs

def read_ascii_file(file):
	file = codecs.open(file,'r',encoding='utf-8',errors='ignore')
	data = file.read()
	rows = data.replace('\r','').split('\n')

	words_origin = ' '.join(rows).split(' ')
	words = ' '.join(rows).lower().split(' ')
	words = sorted(list(set(words)))

	my_data = {}
	for word in words:
		index = []
		for j in range(0,len(rows)):
			if word.lower() in rows[j].lower():
				index.append(str(int(j)+1))
				my_data.update({word:index})

	text = ''
	for key in my_data.keys():
		text=text+key.upper()+' '+','.join(my_data[key])+'\n'

	return text

def write_file(text, file_index):
	file = open('szoveg-index.txt', 'w')
	file.write(text)
	file.close()

if __name__ == "__main__":
	text = read_ascii_file('szoveg.txt')
	write_file(text, 'szoveg-index.txt')