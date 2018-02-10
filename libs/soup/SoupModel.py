import requests
from bs4 import BeautifulSoup


class SoupModel:
    def __init__(self, url):
        request = requests.get(url)
        self._target_url = url
        self._soup = BeautifulSoup(request.content, 'lxml')

    def get_soup(self):
        return self._soup
