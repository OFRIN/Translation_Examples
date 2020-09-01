
import requests
from bs4 import BeautifulSoup

class Daum_Dictionary:
    def __init__(self):
        self.url = 'https://dic.daum.net/search.do?q={}&dic=eng'

    def get(self, word):
        # be%20supposed%20to

        response = requests.get(self.url.format(word))
        soup = BeautifulSoup(response.text, "html.parser")
        
        open('sample_on_daum.html', 'w').write(soup.prettify())

        