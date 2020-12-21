import requests
from bs4 import BeautifulSoup


def search_google(target: str):
    base_url = 'https://www.google.com/search?'
    values = {
        'q': target,
        'oq': target,
        'aqs': 'chrome..69i57j69i59j35i39l2j0i433j69i60l3.1873j0j7',
        'sourceid': 'chrome',
        'ie': 'UTF-8',
    }
    req = requests.get(base_url, params=values)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(req.url)


def search_instagram(target: str):
    '''

    :param target: 검색하고싶은 이름름
   :return: 미정
   https://m.blog.naver.com/a-marketing/220776921315 참고 사이트
   https://top-hashtags.com/instagram/ : top 100 해시태그들
    '''
    base_url = 'https://www.instagram.com/'

    req = requests.get(base_url + target + '/')
    soup = BeautifulSoup(req.content, 'html.parser')
    print(req.url)
