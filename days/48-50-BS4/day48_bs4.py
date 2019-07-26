#!python3

import requests
import bs4

URL = "https://codechalleng.es/bites/"


def pull_site():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/41.0.2228.0 Safari/537.36"}
    raw_site_page = requests.get(URL, headers=headers)
    raw_site_page.raise_for_status()

    return raw_site_page


def scrape(site):
    header_list = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')

    soup.find_all('')
    # html_header_list = soup.select('.')

    # for headers in html_header_list:
    #     header_list.append(headers.getText())
    #
    # for headers in header_list:
    #     print(headers)


if __name__ == '__main__':
    site = pull_site()
    scrape(site)
