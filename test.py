#!/usr/bin/python
import os
#import json
import yaml
#import time
#import ast

#from yaml.loader import SafeLoader

'''
url_list={'KEPI_KEY' : 'https://1', 'KPI_KEY' : 'https://2'}
print(type(url_list))
abc=['KEPI_KEY', 'KPI_KEY']
print(type(abc))

for ele in abc:
    print('ele: ', ele)
    print('url_ele', url_list[ele])


with open('/config.yaml', 'r') as f:
    data=yaml.load(f.read(), Loader=SafeLoader)

print(data)

abc=['KEPI_KEY', 'KPI_KEY']
for ele in abc:
    print('ele: ', ele)
    print('url_ele', data["url_list"][ele])


#code for json
#time.sleep(100000)
print(os.getenv("url_list"))

data=ast.literal_eval(os.getenv("url_list"))
print(type(data))

print(os.getenv("abc"))
data1=ast.literal_eval(os.getenv("abc"))
print(type(data1))

for ele in data:
    print('ele :', ele)
    print(data[ele])

for ele in data1:
    print('ele :', ele)
    print(ele)

# Code for yaml
#time.sleep(100000)
'''

print(os.getenv("url_list"))

config_data=yaml.safe_load(os.getenv("url_list"))
print(type(config_data))
print(" configuration data: ", config_data)

filter_list=yaml.safe_load(os.getenv("filter_list"))
print(type(filter_list))
print(" \n filter data : ",filter_list)


for ele in filter_list:
    print('ele :', ele)
    print(config_data[ele])
'''
for ele in data1:
    print('ele :', ele)
    print(ele)
#time.sleep(100000)
'''
