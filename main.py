import requests
from bs4 import BeautifulSoup

position = 'software+developer'
location = 'Cork'
URL = 'https://ie.indeed.com/jobs?q={}&l={}'.format(position, location)

page = requests.get(URL)
page_soup = BeautifulSoup(page.content, 'html.parser')
jobs = page_soup.find_all(class_='jobsearch-SerpJobCard')
for j in jobs:
    title = j.find('a')['title']
    company = j.find('span', class_="company").text.strip()
    where = j.find(class_="location accessible-contrast-color-location").text.strip()
    summary = j.find_all('li')
    print(title, end=' | ')
    print(where, end=' | ')
    for s in summary:
        print(s.text.strip(), end=' | ')
    print(company, end='\n'*2)
