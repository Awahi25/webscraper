#pip install beautifulsoup4
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')
