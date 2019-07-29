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
    # print(soup)
    soup_found = soup.findAll("div", class_="details_01af72f6")
    # soup_found = soup.select('.details_01af72f6')
    print(soup_found)


if __name__ == '__main__':
    site1 = pull_site()
    scrape(site1)
