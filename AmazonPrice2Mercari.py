from bs4 import BeautifulSoup
import requests
import statistics
import collections

url = 'https://www.mercari.com/jp/search/?keyword='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

query_name = 'tomato'
search_url = url + query_name

r = requests.get(search_url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
price_elements = soup.select('.items-box-price')
prices = []
for element in price_elements:
    price = int(
        element.getText().replace(
            '¥',
            '').replace(
            ' ',
            '').replace(
                ',',
            ''))
    prices.append(price)

print('Search Priduct name : ', query_name)
print('取得できたアイテム数', len(collections.Counter(prices)))

prices.sort()
print('最安値: {:,} 円'.format(prices[0]))
print('平均値: {:,} 円'.format(round(statistics.mean(prices))))
print('最頻値: {:,} 円'.format(collections.Counter(prices).most_common()[0][0]))
print('')
prices.sort(reverse=True)
print('検索対象が含まれていれば反応するので，パッケージ製品の料金が出ている可能性があることに注意してください．')
print('最高値: {:,} 円'.format(prices[0]))
