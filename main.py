import json


# Opening JSON file

u = open('UNIT_DEFINITIONS.json')

units = json.load(u)

for i in units['emp_details']:
    print(i)


u.close()
