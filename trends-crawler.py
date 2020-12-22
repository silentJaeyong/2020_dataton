from selenium import webdriver
from bs4 import BeautifulSoup


def trends(URL):
    # 여기 경로는 각자 selenium chrome path로 설정하면 됨. 동봉한 driver 참고
    driver = webdriver.Chrome(executable_path='C:/Users/SeoKyung/Desktop/말없는재용이/2020_dataton/chromedriver.exe')
    # selenium이 웹 자원이 로드될 때 (3초)까지 기다려줌.
    driver.implicitly_wait(3)
    # chrome 페이지 open
    driver.get(url=URL)
    # open한 페이지를 html화 -> bs로 긁어오기 위해
    html = driver.page_source
    # 위 코드도 가능하지만, lxml이 최근 버전에 호환이 더 잘 된다고 하고, 속도도 빠르다고 해서 lxml사용. 쓰려면 pip로 받아야 함.
    # soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'lxml')
    trends = soup.select('td.main > a')
    # 따온 데이터를 text화 해서 각각 나타내기
    trends_arr = list()
    for i in trends:
        tmp = i.get_text()
        trends_arr.append(tmp)
        print(tmp)
    # 창 닫기
    driver.close()


if __name__ == '__main__':
    trends('https://getdaytrends.com/ko/korea/')
