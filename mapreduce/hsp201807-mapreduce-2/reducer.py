
import sys

sum = 0
current_key = None
social_networks = ["vk", "facebook", "odnoklassniki", "twitter", "reddit"]
c_map = {}

for sn in social_networks:
    c_map[sn] = []

for line in sys.stdin:
    try:
        social, domain, count = line.strip().split('\t')
        count = int(count)
        c_key = (social, domain)
    except ValueError as e:
        continue
    if current_key != c_key:
        
        if current_key:
            assert social in c_map
            c_map[current_key[0]].append((sum, current_key[1]))
            c_map[current_key[0]].sort(reverse=True)
            c_map[current_key[0]] = c_map[current_key[0]][0:10]

        sum = 0
        current_key = c_key

    sum += count


if current_key:
    c_map[current_key[0]].append((sum, current_key[1]))
    c_map[current_key[0]].sort(reverse=True)
    c_map[current_key[0]] = c_map[current_key[0]][0:10]


for sn in social_networks:
    for (sum, domain) in c_map[sn]:
        print(sn + " " + domain + " " + str(sum))
        
