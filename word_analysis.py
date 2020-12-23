# -*- coding: utf-8 -*-
"""word_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ugJ-O5KhO3JkRbMerCMVi10si722MxKx
"""

from konlpy.tag import Hannanum
from collections import Counter
import re
from krwordrank.word import KRWordRank
from nltk import Text
from nltk.tokenize import regexp_tokenize


def remove_special_characters(texts):
    texts = re.sub(
        '[-+=,#/\?:^$!@%&()~]', '', texts
    )
    return texts


def word_analysis(str):

    en = regexp_tokenize(str, "([A-Za-z]+)")
    T=list(Text(en))
    texts = remove_special_characters(str)
    noun = Hannanum().nouns(texts)
    noun.extend(T)
    print(noun)
    count = Counter(noun)
    noun_list = count.most_common(30)
    print(count)
    index = 0
    count_ = []
    for v in noun_list:
        if len(v[0]) >= 1:
            index = index + 1
            count_.append(v)
            if index >= 10:
                break

    return count_


texts = "송고시간2020-12-22 17:38 공유 댓글 글자크기조정 인쇄 백나용 기자백나용 기자 (제주=연합뉴스) read read read 백나용 기자 = 제주도는 22일 0시부터 오후 5시까지 신종 코로나바이러스 감염증(코로나19) 신규 확진자 11명(273∼283번)이 발생했다고 밝혔다.도에 따르면 273번은 7080 라이브 카페 확진자 접촉자로, 274번은 7080 라이브 카페를 방문한 이력이 있다.이에 따라 7080 라이브 카페 관련 확진자는 지난 18일 첫 발생 이후 현재까지 33명으로 늘었다.277번 확진자는 지난 21일 확진 판정을 받은 한국국제교류재단 직원의 접촉자다.277번 확진자는 지난 21일 서울에서 제주로 입도, 제주 입도 후 제주공항 워크스루 선별진료소를 방문해 검체를 채취했다.282번 확진자는 제주 270번 확진자의 가족이다.나머지 확진자 7명에 대해서는 기초 조사가 진행 중이다.아울러 원희룡 제주지사는 이날 오전 코로나19 대책회의를 주재하고 오는 24일부터 전국 모든 식장에서 5인 이상 모임이 전면 금지되는 것과 관련해 세부 지침을 마련하라고 지시했다.특히 원 지사는 이번 조치로 제주로 입도할 예정이었던 입도객이 숙박업소에 대한 예약 취소로 위약금 부담이 발생할 것으로 보고 중앙정부에 전액 환불을 요청해 달라고도 덧붙였다.원 지사는 중앙정부의 5인 이상 집합 금지 조치에 따라 숙박업소에 대한 예약 취소가 속출하고, 이 피해는 고스란히 숙박 예약을 취소한 이들이 받고 있다며 중앙정부의 조치로 피해를 보는 부분은 중앙정부가 책임을 져야 한다고 말했다."
# 텍스트 넣기

word_list = word_analysis(texts)#텍스트 분석해서 키워드 추출
print(word_list)

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def show_word(word_list):
    text = ''
    for word in word_list:
        for num in range(word[1]):
            text = text + ' ' + word[0]
    wc = WordCloud(width=1000, height=600, background_color="white", random_state=0,
                   font_path='MaruBuri-Regular.ttf')
    plt.imshow(wc.generate(text))
    plt.axis("off")
    plt.show()


show_word(word_list)#추출한 리스트를 넣으면 시각적으로 보여줌
