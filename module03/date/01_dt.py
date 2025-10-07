from datetime import datetime, date

# datetime.min = datetime(1, 1, 1)
# datetime.max = datetime(9999, 12, 31, 23, 59, 59, 999999)

d = datetime(year=2022, month=1, day=11, hour=19, second=12)
print(d)
print(d.date())
print(d.time())

print(datetime.now())
print(datetime.today())
