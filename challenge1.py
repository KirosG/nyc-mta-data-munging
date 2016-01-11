import pandas as pd
import numpy as np
import csv
from collections import defaultdict

def mta_csv_to_dict(path_to_csv):
	with open(path_to_csv, 'rb') as csvfile:
	    mta_reader = csv.reader(csvfile, delimiter=',')
	    next(mta_reader, None)
	    
	    mta_dict = defaultdict(list)
	    for row in mta_reader:
	    	row = [element.strip() for element in row]
	        key, val =  tuple(row[:4]), row[4:]
	        mta_dict[key].append(val)
	return dict(mta_dict)

mta_dict = mta_csv_to_dict('mta_data_jan09.csv')

