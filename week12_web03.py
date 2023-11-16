#파이썬에서 자료 다루는 것: 리스트, 딕셔너리
from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href = "http://www.daelim.ac.kr">대림대학교</a><br>
<a href = "http://www.harvard.edu">하버드대학교</a><br>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a")
print(urls)
# from bs4 import BeautifulSoup
# html = """
# <html>
# <head>
# <title>스크레이핑 실습</title>
# </head>
# <body>
# <h1 id="univ">대림대학교</h1>
# <p>웹스크레이핑</p>
# <p id="contents">파이썬, 판다스, 넘파이, 맷플롯립, GUI...</p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html, 'html.parser')
# university = soup.find(id='univ')
# contents = soup.find(id='contents')
#
# print(university)
# print(contents)
# print(contents.string)