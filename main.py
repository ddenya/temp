import requests
import json

def get_data(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"Failed to get the data. Code {response.status_code}")
      return None
  except Exception as e:
    print(f"Something happened: {str(e)}")
    return None
  
url = "https://jsonplaceholder.typicode.com/todos"
json_data = get_data(url)
#print(json.dumps(json_data, indent=4))

if json_data:
  string = 'qui'
  filtered_data = [item['title'] for item in json_data if string in item['title']]
else:
  print(f'No filtering because there is no data to filter')

for title in filtered_data:
  if isinstance(title, int):
    print(f'{title} is an int')
  else:
    print(f'{title}')