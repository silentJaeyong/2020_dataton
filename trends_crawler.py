from selenium import webdriver
from bs4 import BeautifulSoup
import tweepy
import threading


class twitter:
    api = None
    result_file = []

    def __init__(self):
        consumer_key = 'MEkO26YccoCAZLzKnYtY9zpHZ'
        consumer_secret = 'LMaFEAMMyblIoboDfQIEeRLcDyWNQqXPmplujLogJtXwIruSYv'
        access_token = '1324111638673305600-7cqll3GwZHAGPRYNVqz4meL7pS3eaE'
        access_secret = 'fZuubaUVDrBhAg3VXnVDdnoXigmdtA1YEoOoZDK253WYY'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth)
        print('twitter API connected!')

    def trends(self, url):
        # 여기 경로는 각자 selenium chrome path로 설정하면 됨. 동봉한 driver 참고
        driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        # selenium이 웹 자원이 로드될 때 (3초)까지 기다려줌.
        driver.implicitly_wait(3)
        # chrome 페이지 open
        driver.get(url=url)
        # open한 페이지를 html화 -> bs로 긁어오기 위해
        html = driver.page_source
        # 위 코드도 가능하지만, lxml이 최근 버전에 호환이 더 잘 된다고 하고, 속도도 빠르다고 해서 lxml사용. 쓰려면 pip로 받아야 함.
        # soup = BeautifulSoup(html, 'html.parser')
        soup = BeautifulSoup(html, 'lxml')
        trends = soup.select('td.main > a')
        # 따온 데이터를 text화 해서 각각 나타내기
        trends_arr = []
        for i in trends:
            tmp = i.get_text()
            trends_arr.append(tmp)
        # 창 닫기
        driver.close()
        return trends_arr
        print('twitter trends crawl done!')

    def init_work(self, trends: list):
        print("Start working...")
        for trend in trends:
            t = threading.Thread(target=self.search_keyword, args=(trend,))
            t.start()

    def search_keyword(self, keyword: str):
        for tweet in tweepy.Cursor(self.api.search, q=keyword, lang='ko', include_entities=False).items(10000):
            if "RT" not in tweet.text:
                line = [keyword, str(tweet.created_at), tweet.text]
                # line.append(핵심단어)
                self.result_file.append(line)
        print(f"keyword : {keyword} search done!")
