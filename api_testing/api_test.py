import requests

headers = {
    'X_CP-API-ID': 'xxxxx',
    'X-CP-API-KEY': 'xxxxx',
    'X-ECM-API-ID': 'xxxxx',
    'X-ECM-API-KEY': 'xxxxx',
}

req = requests.get('https://cradlepointecm.com/api/v2/routers/', headers=headers)
print(req)
