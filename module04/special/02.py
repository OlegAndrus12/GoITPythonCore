# importing datetime object
from datetime import datetime, tzinfo
from dateutil import tz

# from dateutil.zoneinfo import get_zonefile_instance
# zonenames = list(get_zonefile_instance().zones)
# print(zonenames)


# defining the object
obj = datetime.now(tz=tz.gettz('Poland'))

# checking timezone information
print(obj.tzinfo)
print(obj)
