import requests
from bs4 import BeautifulSoup

class Naver_Dictionary:
    def __init__(self):
        self.url = "http://endic.naver.com/search.nhn?query="
        
    def get(self, word):
        response = requests.get(self.url + word)
        # soup = BeautifulSoup(response.content, "html.parser")
        soup = BeautifulSoup(response.text, "html.parser")

        for obj in soup.select('div > p > a'):
            print(obj.text)
        
        open('sample_from_text.html', 'w').write(soup.prettify())

        