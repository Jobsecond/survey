# coding: utf-8
from __future__ import division, print_function
from collections import OrderedDict
import xlrd
import pandas


data = xlrd.open_workbook(r'raw_data.xlsx')
table = data.sheets()[0]
#print(table.col_values(1))
number_of_options = [4, 3, 4, 5, 5, 6, 4, 3, 3, 2]
l = []
for i in range(len(number_of_options)):
    d = OrderedDict()
    for option in [unichr(x) for x in range(65, 65 + number_of_options[i])]:
        d[option] = 0
        for j in range(1, table.nrows):
            if unicode(table.col(i+1)[j].value).find(option) >= 0:
                d[option] += 1
    l.append(d)
print(pandas.DataFrame(l, index=range(1,11)).fillna(''))
