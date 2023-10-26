import urllib.request

url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/m/logo.png'
# urllib.request.urlretrieve(url, 'daelim.png') #이미지를 다운 받고 보조기억장치에 저장
# print("저장완료")
logo = urllib.request.urlopen(url).read() #이미지를 다운 받고 메모리에 저장

with open('dealim.png', "wb") as file: #원본 이미지가 png 포맷이므로 쓰기 모드5ㅇ
    file.write(logo)
    print("저장완료")
