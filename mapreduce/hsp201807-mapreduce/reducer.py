
import sys

word_sum = 0
word_dic = {}

current_key = None

for line in sys.stdin:
    try:
        c_key, word, count = line.strip().split('\t')
        count = int(count)
    except ValueError as e:
        continue
    if current_key != c_key:
        
        if current_key:
            str_to_print = ""
            for mkey, mvalue in sorted(word_dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                str_to_print += mkey +":"+str(mvalue)+";"
            print(current_key + "\t" + str(word_sum) + "\t" + str_to_print)

        word_sum = 0
        current_key = c_key
        word_dic = {}

    
    word_sum += count
    if word in word_dic:
        word_dic[word] += count
    else:
        word_dic[word] = count


if current_key:
    str_to_print = ""
    for mkey, mvalue in sorted(word_dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        str_to_print += mkey +":"+str(mvalue)+";"
    print(current_key + "\t" + str(word_sum) + "\t" + str_to_print)


