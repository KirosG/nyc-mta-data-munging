from challenge2 import mta 
import dateutil.parser
import datetime




def find_min_daily_values(mta_value_list):
	min_hour_dict = {}
	for i in mta_value_list:
	    if i[0].date() not in min_hour_dict:
	        min_hour_dict[i[0].date()] = i[1]
	    else:
	        min_hour_dict[i[0].date()] = min(i[1],min_hour_dict[i[0].date()])
	return min_hour_dict

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

def mta_to_timeseries(mta_data):
	ts = {}
	for key in mta_data.keys():
		ts_hourly_cumulative = mta_data[key]
		ts_daily_cumulative = find_min_daily_values(ts_hourly_cumulative)
		ts_daily_totals = decumulate(ts_daily_cumulative)
		ts[key] = [[k,v] for k,v in ts_daily_totals.items()]
	return ts

ts_mta = mta_to_timeseries(mta)

