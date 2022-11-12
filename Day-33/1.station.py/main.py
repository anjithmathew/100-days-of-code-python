import requests
import json
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data_unformated = response.json()

data_formated = json.dumps(data_unformated)

print(data_formated)

# print(data['iss_position']['longitude'])
