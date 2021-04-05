###Credit for this scraper goes to Aleksa Tamburovski##
#If you are learning Python, I highly recommend his courses#

from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup
import requests #https://docs.python-requests.org/en/master/
import requests.exceptions #https://2.python-requests.org/en/v3.0.0/api/#requests.RequestException
import urllib.parse #https://docs.python.org/3/library/urllib.parse.html
from collections import deque #https://docs.python.org/3/library/collections.html#collections.deque
import re #https://docs.python.org/3/library/re.html

user_url = str(input('[+] Enter Target URL to Scan: '))
urls = deque([user_url])

scraped_urls = set()
emails = set()

count = 0

#This section is for populating our 'scraped_urls' set
try:
    while len(urls):
        count +=1
        if count == 100: #scrapes only first 100 URLs
            break
        url = urls.popleft()
        scraped_urls.add(url)

#All emails found in URLs save and print to screen
        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netlock}'.format(parts)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', response.text, re.I)) # regex - how we search for emails (everything before '@', everything after '@') & how we save them in response.text
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features='lxml')

        for anchor in soup.find_all('a'):
            lilnk = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print('mail')
