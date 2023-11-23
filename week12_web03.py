import urllib.request

import pandas
from bs4 import BeautifulSoup
import pandas as pd
import datetime

shops = list()

for i in range(1, 52):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    print(url)
    page = urllib.request.urlopen(url) #다운로드 역할
    soup = BeautifulSoup(page, 'html.parser') #soup 객체에 넣고 분석할 준비
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr') #모든 tr 태그를 리스트로

    for tr in trs: #각 매장의 정보
        tds = tr.find_all('td') #td 전부
        shop_name = tds[1].string #매장 이름
        shop_addr = tds[3].string #매장 주소
        shop_tel = tds[5].string #매장 번호

        shops.append([shop_name]+[shop_addr]+[shop_tel]+[datetime.datetime.now()]) #이차원 리스트 생성, 이차원 리스트로 만들어서 판다스를 사용하기 위해

# print(shops)

holly_df = pandas.DataFrame(shops, columns = ('매장명', '주소', '전화번호', '일시'))
holly_df.to_csv('holly.csv', mode ="w", encoding='cp949')
#데이터 프레임에 넣으려고 2차원 리스트로 만듬

#ndarray 자료를 사용함, 메모리 사용량이 적음
#넘파이 배열은 반복문 없이도 수학적 계산 가능

