import re


ips = {}

file = open("logs.txt", "r")
for log_line in file.readlines():
    match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", log_line)
    key = match.group(0)
    if key not in ips.keys():
        ips[key] = 1
    else:
        ips[key] = ips[key] + 1

res_len = len(ips.keys())
results = sorted(ips.items(), key=lambda x: x[1], reverse=True)[:res_len]
print(results)
