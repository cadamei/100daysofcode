#!python3

import bs4
import os

FILE = 'dd.html'

base_folder = os.path.dirname(__file__)
file_path = os.path.join(base_folder, FILE)


def pull_site():
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) "
    #                          "AppleWebKit/537.36 (KHTML, like Gecko) "
    #                          "Chrome/41.0.2228.0 Safari/537.36"}
    # raw_site_page = requests.get(file_path, headers=headers)
    # raw_site_page.raise_for_status()

    with open('dfhhdgh', 'r', encoding='utf-8') as raw_data:
        print(file_path)
        print(base_folder)
        print(type(raw_data.read()))
        print(raw_data.read())

        return raw_data.read()


def scrape(site):
    # header_list = []

    soup = bs4.BeautifulSoup(site, 'html.parser')
    print(soup)
    #
    # print(soup.find_all('div'))
    # html_header_list = soup.select('.details_01af72f6')
    #
    # for headers in html_header_list:
    #     header_list.append(headers.getText())
    #
    # for headers in header_list:
    #     print(headers)


if __name__ == '__main__':
    site1 = pull_site()
    scrape(site1)
