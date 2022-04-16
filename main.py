import typing

import requests
from bs4 import BeautifulSoup


class Site:
    def __init__(self):
        self.session = requests.session()
        cookies = {
            'PHPSESSID': 'sgn3atogn68t2qpslvg7id8s5e',
            'LIVECHAT_GUEST_HASH': '43c77722bf4768edd8786f7f768c2507',
            'BITRIX_SM_GUEST_ID': '548453',
            '_ym_uid': '1650140368404270683',
            '_ym_d': '1650140368',
            '_ga': 'GA1.2.2103646024.1650140368',
            '_gid': 'GA1.2.80411256.1650140368',
            '_ym_visorc': 'w',
            '_ym_isad': '1',
            'BX_USER_ID': 'e17009627d799679af36f4a1052ded53',
            'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1650142740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
            '_gat_gtag_UA_99250594_2': '1',
            'BITRIX_SM_LAST_VISIT': '16.04.2022%2023%3A22%3A51',
        }

        headers = {
            'authority': 'decor-magic.ru',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://away.vk.com/',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'PHPSESSID=sgn3atogn68t2qpslvg7id8s5e; LIVECHAT_GUEST_HASH=43c77722bf4768edd8786f7f768c2507; BITRIX_SM_GUEST_ID=548453; _ym_uid=1650140368404270683; _ym_d=1650140368; _ga=GA1.2.2103646024.1650140368; _gid=GA1.2.80411256.1650140368; _ym_visorc=w; _ym_isad=1; BX_USER_ID=e17009627d799679af36f4a1052ded53; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1650142740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _gat_gtag_UA_99250594_2=1; BITRIX_SM_LAST_VISIT=16.04.2022%2023%3A22%3A51',
        }

        params = {
            'PAGE_EL_COUNT': 'ALL',
        }

        content = self.session.get('https://decor-magic.ru/catalog/pokryvala_odnospalnye/', headers=headers,
                                   params=params, cookies=cookies).content

        soup = BeautifulSoup(content)
        products: typing.List[Product] = []
        for i in soup.find_all(class_='products-flex-item'):
            prod = Product(i.find('a').attrs['href'])
            prod.take_stats()
            products.append(prod)
            print(1)
        """Сюда дописать код для сохранения всего"""
        print(1)


class Product:
    def __init__(self, url):
        self.url = "https://decor-magic.ru" + url

    def take_stats(self):
        cookies = {
            'PHPSE-SSID': 'sgn3atogn68t2qpslvg7id8s5e',
            'LIVECHAT_GUEST_HASH': '43c77722bf4768edd8786f7f768c2507',
            'BITRIX_SM_GUEST_ID': '548453',
            '_ym_uid': '1650140368404270683',
            '_ym_d': '1650140368',
            '_ga': 'GA1.2.2103646024.1650140368',
            '_gid': 'GA1.2.80411256.1650140368',
            '_ym_visorc': 'w',
            '_ym_isad': '1',
            'BX_USER_ID': 'e17009627d799679af36f4a1052ded53',
            'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1650142740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
            'BITRIX_SM_LAST_VISIT': '16.04.2022%2023%3A23%3A35',
        }

        headers = {
            'authority': 'decor-magic.ru',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://decor-magic.ru/catalog/pokryvala_odnospalnye/?PAGE_EL_COUNT=ALL',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'PHPSESSID=sgn3atogn68t2qpslvg7id8s5e; LIVECHAT_GUEST_HASH=43c77722bf4768edd8786f7f768c2507; BITRIX_SM_GUEST_ID=548453; _ym_uid=1650140368404270683; _ym_d=1650140368; _ga=GA1.2.2103646024.1650140368; _gid=GA1.2.80411256.1650140368; _ym_visorc=w; _ym_isad=1; BX_USER_ID=e17009627d799679af36f4a1052ded53; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1650142740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BITRIX_SM_LAST_VISIT=16.04.2022%2023%3A23%3A35',
        }

        response = requests.get(self.url, headers=headers, cookies=cookies)

        soup = BeautifulSoup(response.content)
        atr = soup.find('table').find_all('tr')
        self.design = atr[0].contents[1].contents
        self.compound = atr[1].contents[1].contents
        self.size = atr[2].contents[1].contents
        self.mass_brutto = atr[3].contents[1].contents
        self.pack_size = atr[4].contents[1].contents
        self.contry = atr[5].contents[1].contents


Site()
