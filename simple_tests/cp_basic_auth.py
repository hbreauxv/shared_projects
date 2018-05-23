import requests

cp_get = requests.get('https://174.148.47.148/api/status/system/cpu', auth=('admin','11'))

print(cp_get)
