import sys
import re
import string

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

exclude = set(string.punctuation)

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
        for x in '.,!?:;':
            text = text.replace(x, '')
    except ValueError as e:
        continue
    words = text.split()
    for word in words:
        if len(word) < 3:
            continue
	word = word.lower()
        sorted_word = ''.join(sorted(word))
        
        print(sorted_word + "\t" + word + "\t" + str(1))

