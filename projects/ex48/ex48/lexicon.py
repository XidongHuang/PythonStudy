"""*************************************************************************
    > File Name: lexicon.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Wed 12 Oct 20:53:48 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

direction=['north', 'south','east']
verb = ['go', 'kill', 'eat']
stop = ['the', 'in', 'of']
nouns = ['bear', 'princess']
number = range(999999)

vocabulary={'direction': direction, 'noun': nouns, 'verb': verb, 'stop': stop, 'number': number}

def scan(sentence):
	words = sentence.split()
	result = []
	for word in words:
		found = False
		for key,value in vocabulary.items():
			if word.lower() in value:
				result.append((key, word))
				found = True
				break
		
		if not found:
			try:
				for key, value in vocabulary.items():
					num_word = int(word)
					if num_word in value:
						result.append((key, num_word))
						break
			except ValueError:
				result.append(('error', word))
		
	return result
