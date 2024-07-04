import json
import csv

with open('users_data_12;05;21.json', 'r') as file:
    data = json.load(file)

rows = []
for user in data['data']:
    rows.append(list(user.values()))
rows = [list(data['data'][0].keys())] + rows

with open('users_data_{date}.csv'.format(date=data['current_date']), 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in rows:
        csv_writer.writerow(row)

