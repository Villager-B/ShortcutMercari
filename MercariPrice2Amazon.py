'''
MerucariPrice2Amazon
'''

from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.co.jp/s?k='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

query_name = 'tomato'
search_url = url + query_name

r = requests.get(search_url, headers=headers)

print('Search Priduct name : ', query_name)

soup = BeautifulSoup(r.content, "html.parser")
item_root_elements = soup.find_all(
    class_='sg-col-inner')

print('item length : ', len(item_root_elements))

name_list = []
price_list = []

for item_root_element in item_root_elements:
    if item_root_element.find(
        class_='a-size-base-plus a-color-base a-text-normal') and item_root_element.find(
            class_='a-price-whole'):
        item_name = item_root_element.find(
            class_='a-size-base-plus a-color-base a-text-normal')

        item_price = item_root_element.find(
            class_='a-price-whole')
        name_list.append(item_name.getText())
        price_list.append(item_price.getText())
    else:
        continue

print('getItem length : ', len(name_list))

if len(name_list) >= 5:
    print('検索結果を5件表示します')
    for i in range(5):
        print('name[', i + 1, '] : ', name_list[i])
        print('price[', i + 1, '] : ', price_list[i], '\n')
else:
    for i in range(len(name_list)):
        print('name[', i + 1, '] : ', name_list[i])
        print('price[', i + 1, '] : ', price_list[i], '\n')
