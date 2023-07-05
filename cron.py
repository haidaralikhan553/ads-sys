import requests

def main():
    # login and get access token
    url = "http://127.0.0.1:8000/api/auth/login/"
    res = requests.post(url, data={'username': 'jawad', 'password': 'jawad'})
    access = 'JWT ' + res.json()['access']
    headers = {'Authorization': access}

    # reset all counts
    url = "http://127.0.0.1:8000/api/ads/resetall/"
    res = requests.get(url, headers=headers)
    print(res.json())

if __name__ == '__main__':
    main()