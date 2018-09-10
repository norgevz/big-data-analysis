import sys
import re
import string

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

exclude = set(string.punctuation)

for line in sys.stdin:
    try:
        url , text = unicode(line.strip()).split('\t', 1)
        domain = url.split('/')[2]
        if domain.startswith("www."):
            domain = domain[4:]        
        
        tokens = text.split(";")
        for tok in tokens:
            sn, cnt = tok.split(":")
            print(sn + "\t" + domain + "\t" + str(cnt))
       
    except ValueError as e:
        continue
    

