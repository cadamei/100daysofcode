#!python3

import feedparser
import smtplib
import requests

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from argparse import ArgumentParser

FEED_FILE = "feed.xml"
URL = "https://talkpython.fm/episodes/rss"


def get_rss():
    r = requests.get(URL)
    with open('feed.xml', 'wb') as f:
        f.write(r.content)


def email_ep(app_pass):
    from_addr = 'johnathan.st@gmail.com'
    to_addr = 'johnathan.st@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'New episode from Talk Python to Me is available'

    body = input("Enter the body of the email:\n")

    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

    smtp_server.ehlo()

    smtp_server.starttls()

    smtp_server.login(from_addr, app_pass)

    text = msg.as_string()

    smtp_server.sendmail(from_addr, to_addr, text)

    smtp_server.close()


def parse_rss():
    feed = feedparser.parse(FEED_FILE)

    with open('episodes.txt', 'a') as f:
        if 'title' in feed.entries[0]:
            for entry in feed.entries:
                f.write(entry.title + ": " + entry.link + '\n')

    if 'title' in feed.entries[0]:
        for entry in feed.entries:
            print(entry.published + " - " + entry.title + ": " + entry.link)


def main():
    parser = ArgumentParser(description="RSS Emailer!")
    parser.add_argument('app_pass', help="The Gmail app password")

    args = parser.parse_args()

    get_rss()

    parse_rss()

    email_ep(args.app_pass)


if __name__ == '__main__':
    # main()
    get_rss()
    parse_rss()
