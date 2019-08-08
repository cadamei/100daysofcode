import requests

URL = "https://talkpython.fm/episodes/rss"

if __name__ == '__main__':
    r = requests.get(URL)
    with open('neweps', 'wb') as f:
        f.write(r.content)