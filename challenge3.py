from challenge2 import mta 
import dateutil.parser


k = mta.keys()[0]
ts = mta[k]

d = {}
for i in ts:
    if i[0].date() not in d:
        d[i[0].date()] = i[1]
    else:
        d[i[0].date()] = min(i[1],d[i[0].date()])

