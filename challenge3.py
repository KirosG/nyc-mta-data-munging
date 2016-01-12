from challenge2 import mta 
import dateutil.parser
import datetime


k = mta.keys()[0]
ts = mta[k]

d = {}
for i in ts:
    if i[0].date() not in d:
        d[i[0].date()] = i[1]
    else:
        d[i[0].date()] = min(i[1],d[i[0].date()])

def decumulate(mta_dict):
	new_dict = {}
	for day in mta_dict.keys():
		next_day = day + datetime.timedelta(days=1)
		if next_day not in mta_dict:
			day_to_delete = day
		else:
			new_value = int(mta_dict[next_day]) - int(mta_dict[day])
			new_dict[day] = new_value
	return new_dict
