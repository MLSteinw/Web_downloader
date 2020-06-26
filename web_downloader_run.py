import requests

if __name__ == '__main__':
    url = 'https://ucdavis.app.box.com/folder/68864389765'
    geturl = requests.get(url, allow_redirects=True)
    print(geturl.headers.get('content-type'))


# Test version control