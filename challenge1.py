# Download a few MTA turnstile data files
# Open up a file, use csv reader to read it, 
# make a python dict where there is a key for each (C/A, UNIT, SCP, STATION).
# These are the first four columns. 
# The value for this key should be a list of lists. 
# Each list in the list is the rest of the columns in a row. 


import pandas as pd

df = pd.read_csv('mta_data_jan09.csv')
df.head()



