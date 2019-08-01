#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv, os

for filename in os.listdir('./csv'):
    city = filename.split('.')[0]
    print(city)
    with open('./csv/' + city + '.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        with open('./output/' + city + '.csv', 'w', newline='') as f_ouput:
            writer = csv.writer(f_ouput)
            writer.writerow(['date', 'score'])
            for row in reader:
                print([row[1], row[3]])
                writer.writerow([row[1], row[3]])
            f_ouput.close()
            f.close()
