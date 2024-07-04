import random
import datetime
import json

users = ['Arthur', 'Kate', 'Alice', 'Mike']
users_list = []
for user in users:
    users_list.append({'name': user, 'age': random.randint(1, 99)})
data = {
    'data': users_list,
    'current_date': datetime.datetime.now().strftime('%d;%m;%y')
}
filename = 'users_data_{current_date}.json'.format(
    current_date=data['current_date']
)
with open(filename, 'w') as json_file:
    json.dump(data, json_file)
