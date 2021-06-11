"""
Anonymous Command Line Browser

Created: 06.08.2021
Last Updated: 06.08.2021
Author: Anonymous One

Dependencies: None

Notes: Refactor to class with requests.Session
"""


from requests import get, exceptions
import re


def valid_url(url):
    """URL Validator"""
    regex = re.compile(
                    r'^(?:http|ftp)s?://'  # http:// or https://
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                    r'localhost|'  # localhost...
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                    r'(?::\d+)?'  # optional port
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def browser(url='https://api.anonsys.tech/ip/', proxies={'http': None, 'https': None, 'ftp': None}, headers=None):
    if not valid_url(url):
        print(f"URL is not valid: {url}")
        quit()
    try:
        request = get(url=url, proxies=proxies)
        response = request.content
        print(response)
    except exceptions.ProxyError as e:
        print(f"Request failed due to proxy: {proxies}\n{e}")


if __name__ == '__main__':
    proxies = {'http': 'http://203.243.63.16}',
               'https': 'http://217.79.181.109:443'}
    browser(proxies=proxies)
