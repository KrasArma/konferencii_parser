from urllib.request import urlopen
from urllib.parse import quote
import re
print('Введите полное название конфеленции')
res = input()
url = 'https://konferencii.ru/list?search%5Bkeywords%5D=' + quote(res)
print(url)
html = urlopen(url).read().decode('utf-8')
date = re.findall(r'\d{2}\s\w+\s\d{4}\s\S{2}\s+\S\s+\d{2}\s\w+\s\d{4}\s\S{2}', html)
print(date)