import collections

"""
# Dictionary Initialization
Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}

# taking list of car values in v
v = list(Company.values())

# taking list of car keys in v
k = list(Company.keys())

print(k[v.index(max(v))])



# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}

Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)
"""

temperatures = [0.5, 0.0, -3.5, 0.0, 2.5, 3.5, 4.0, 0.5, 3.5, 5.5, 6.0, 10.0, 12.5]

t_count = collections.Counter(temperatures)
print(t_count)
print(t_count.most_common())
print(t_count.most_common())
