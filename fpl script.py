from urllib import response
import requests, os
import json
from dotenv import load_dotenv

session = requests.session()
gameweek = int(input('enter gameweek: '))

load_dotenv()
MANAGER_ID = os.getenv('MANAGER_ID')

response = session.get('https://fantasy.premierleague.com/api/entry/{}/history/'.format(MANAGER_ID))

d = json.loads(response.text)
print(d['current'][gameweek-1]['points'])


