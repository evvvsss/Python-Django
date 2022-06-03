import sys
import requests
from bs4 import BeautifulSoup


class Roads:
    def __init__(self):
        self.prev = []

    def search(self, path: str):
        res = None
        URL = f'https://en.wikipedia.org/{path}'
        try:
            res = requests.get(url=URL)
            res.raise_for_status()
        except requests.HTTPError as e:
            if res.status_code == 404:
                print("It's a dead end !")
            else:
                print(e)
            return
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        if title in self.prev:
            print("It leads to an infinite loop !")
            return
        self.prev.append(title)
        print(title)
        if title == 'Philosophy':
            print(f"{len(self.prev)} roads from {self.prev[0] if len(self.prev) > 0 else 'Philosophy'} to Philosophy")
            return
        content = soup.find(id='mw-content-text')
        all_links = content.select('p > a')
        for link in all_links:
            if link.get('href') is not None and link['href'].startswith('/wiki/') \
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                self.search(link['href'])
                return
        print("It leads to a dead end !.")
        return


def main():
    wiki = Roads()
    if len(sys.argv) == 2:
        wiki.search('/wiki/'+sys.argv[1])
    elif len(sys.argv) == 2:
        print('one argument required! : title')
    else:
        print('wrong argument count!')


if __name__ == '__main__':
    main()
