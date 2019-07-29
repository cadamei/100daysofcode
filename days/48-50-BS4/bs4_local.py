#!python3
import bs4
import os
import re

FILE = "dd.html"
base_folder = os.path.dirname(__file__)
file_path = os.path.join(base_folder, FILE)


def pull_site():
    with open(file_path, 'r', encoding='utf-8') as raw_data:
        page_content = raw_data.read()

        return page_content


def scrape(site):
    soup = bs4.BeautifulSoup(site, 'html.parser')
    soup_found = soup.find_all('a',
                               {'href': re.compile(r'https://nttlimited-my\.sharepoint\.com/person\.aspx\?user=.*')})
    print(soup_found)

    names = [name.getText() for name in soup_found if name.getText()]
    for name in names:
        print(name)


if __name__ == '__main__':
    site1 = pull_site()
    scrape(site1)
