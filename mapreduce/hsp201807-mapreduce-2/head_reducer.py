from __future__ import print_function
import sys
social_networks = ["vk", "facebook", "odnoklassniki", "twitter", "reddit"]
c_map = {}
for sn in social_networks:
    c_map[sn] = []

for line in sys.stdin:
    sn, domain, count = line.split()
    count = int(count)
    c_map[sn].append((count, domain))

for sn in social_networks:
    c_map[sn].sort(reverse=True)
    for (cnt, domain) in c_map[sn][:10]:
        print(sn + " " + domain + " " + str(cnt))


