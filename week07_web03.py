from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1>대림대학교</h1>
<p>웹 스크레이핑</p>
<p>python 기초 문법, 넘파이, 판다스, 맷플로우, 사이킷런, gui ... </p>
<a href = "http://www.daelim.ac.kr">대림대학교</a>
<a href = "http://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
# t = soup.html.head.title.string
# h1 = soup.html.body.h1.string
# p1 = soup.html.body.p
# p2 = p1.next_sibling.next_sibling
urls = soup.find_all("a")
print(urls)
for url in urls:
    univ = url.string
    link = url.attrs['href']

    print(f'{url.string}의 url 주소는 {url.attrs["href"]}입니다.')
    print(univ)
    print(link)
