#pip install requests
import requests

url = 'https://business.gc-chamber.com/list/searchalpha/a'

r = requests.get(url)

print(r.content[:100])
