import requests

headers = {
    'X_CP-API-ID': '80780c4c',
    'X-CP-API-KEY': '0c384093805172f14a99670d96b8f190',
    'X-ECM-API-ID': 'efb75e45-e534-4639-8e9c-a0f57579cdd8',
    'X-ECM-API-KEY': '0e0fc3a4ebba4467690e561da72b49a9e2f77cea',
}

req = requests.get('https://cradlepointecm.com/api/v2/routers/', headers=headers)
print(req)