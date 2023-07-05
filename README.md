# ads-sys

1. Login using requests:
url = "http://127.0.0.1:8000/api/auth/login/"
res = requests.post(url, data={'username': 'jawad', 'password': 'jawad'})
access = 'JWT ' + res.json()['access']
refresh = res.json()['refresh']

2. Refresh Token:
url = "http://127.0.0.1:8000/api/auth/refresh/"
headers = {'Authorization': access}
res = requests.post(url, data={'refresh': refresh}, headers=headers)

3. Logout:
url = "http://127.0.0.1:8000/api/auth/logout/"
res = requests.post(url, data={'refresh': refresh})

4. Admin post an ad:
url = "http://127.0.0.1:8000/api/ads/"
res = requests.post(url, data={'ad_name': "temp ad 003"}, headers=headers)

5. Update an ad:
url = "http://127.0.0.1:8000/api/ads/<id>/"
res = requests.post(url, data={'ad_name': "temp ad 003 updated"}, headers=headers)

6. Delete an ad:
url = "http://127.0.0.1:8000/api/ads/<id>/"
res = requests.delete(url, headers=headers)

7. View an ad:
url = "http://127.0.0.1:8000/api/ads/<id>/"
res = requests.get(url, params={'location': 'khi'})

for i in range(200):
    res = requests.get(url, params={'location': 'khi'})
    print(res.json())

for i in range(101):
    res = requests.get(url, params={'location': 'lhr'})
    print(res.json())

8. Admin to reset counter:
url = "http://127.0.0.1:8000/api/ads/3/reset/"
res = requests.get(url, params={'location': 'lhr'}, headers=headers)

9. Admin can reset all counts:
url = "http://127.0.0.1:8000/api/ads/resetall/"
res = requests.get(url, headers=headers)

10. Cron job python file is defined in the root of project folder.