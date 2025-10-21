import re
from collections import defaultdict, Counter


# replace dict with defaultdict
# use context manager
# compile regex
# no need for "r"
# do i need search? why not find_all
# can i use then Counter with most common?
# what if file is too big?

# ips = defaultdict(int)

with open("logs.txt", "r") as log_file:
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    ips = re.findall(pattern, log_file.read())
    results = Counter(ips)

    print(results)
    print(results.most_common(10))