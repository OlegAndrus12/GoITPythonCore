import re
from collections import Counter

pattern = re.compile(r"(\d{1,3}(?:\.\d{1,3}){3})")

def ip_generator(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield from re.findall(pattern, line)

# Use Counter directly on the generator
results = Counter(ip_generator("logs.txt"))

print(results)
print(results.most_common(10))