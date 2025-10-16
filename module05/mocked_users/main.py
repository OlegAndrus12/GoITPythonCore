from mock import get_mocked_user
import json

filename = input("Enter filename >>> ")
amount = int(input("How many fake users you want >>> "))

mocked_users = list()
for i in range(amount):
    mocked_users.append(get_mocked_user())


with open(filename, "w") as file:
    json.dump(mocked_users, file, indent=4)
