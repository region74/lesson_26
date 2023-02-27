import requests
import pprint

# response = requests.get('http://127.0.0.1:8000/categories/categories/')
# response = requests.get('http://127.0.0.1:8000/api/ver1/tags/',auth=('admin','3434548'))

token = 'c9d29622b86b48f85880a64cc2890485bdf61c65'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/ver1/tags/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/ver1/tags/')
pprint.pprint(response.json())
