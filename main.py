# This is a sample Python script.

import json
import statistics
from urllib.parse import unquote
import requests
from selectolax.parser import HTMLParser
from statistics import mean
import statistics
statistics


# def get_json(url):
#     data = {}
#
#     response = requests.get(url=url)
#     html = response.text
#
#     tree = HTMLParser(html)
#     scripts = tree.css('script')
#     for script in scripts:
#         if 'window.__initialData__' in script.text():
#             jsontext = script.text().split(';')[0].split('=')[-1].strip()
#             jsontext = unquote(jsontext)
#             jsontext = jsontext[1:-1]
#
#             data = json.loads(jsontext)
#
#     return data
#
#
# def get_offers(data):
#     offers = []
#     for key in data:
#         if 'single-page' in key:
#             items = data[key]["data"]["catalog"]["items"]
#             for item in items:
#                 if item.get("id"):
#                     offer = item["normalizedPrice"]
#                     offers.append(offer)
#
#     return offers
#
#
# def main():
#     url = 'https://www.avito.ru/mytischi/kvartiry/prodam-ASgBAgICAUSSA8YQ?p=1&s=104'
#     data = get_json(url)
#     offers = get_offers(data)
#     print(offers)
    # for offer in offers:
    #     s = offer
    #
    #     c = (s.split('₽ за м²')[0])
    #     b = c.split()
    #     b = ''.join(b)


def get_html(url):
    response = requests.get(url=url)
    html = response.text

    tree = HTMLParser(html)
    scripts = tree.css('script')
    for script in scripts:
        if 'window.__initialData__' in script.text():
            print(script.text())



def main():
    url = 'https://www.avito.ru/stavropol/kvartiry/prodam-ASgBAgICAUSSA8YQ?s=104'
    get_html(url)




if __name__ == '__main__':
    main()
