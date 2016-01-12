import csv
from collections import defaultdict
import dateutil.parser

def mta_csv_to_timeseries(path_to_csv):
	with open(path_to_csv, 'rb') as csvfile:
	    mta_reader = csv.reader(csvfile, delimiter=',')
	    next(mta_reader, None)
	   
	    mta_dict = defaultdict(list)
	    for row in mta_reader:
	    	row = [element.strip() for element in row]
	        key, datetime, entries =  tuple(row[:4]), dateutil.parser.parse(row[6] +' '+ row[7]), row[9]
	        mta_dict[key].append([datetime,entries])
	return dict(mta_dict)

mta = mta_csv_to_timeseries('mta_data_jan09.csv')