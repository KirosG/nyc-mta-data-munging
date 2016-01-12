from challenge2 import mta 

k = mta.keys()[0]

x = mta[k]

# dates = set([i[0] for i in x ])

date_totals_dict = {}

for i in x:
	if i[0] not in date_totals_dict:
		date_totals_dict[i[0]] = int(i[2])
	else:
		date_totals_dict[i[0]] += int(i[2])

x = date_totals_dict
print date_totals_dict.keys()




# x = mta[key]
# x = ''
# mta[key] = x 

