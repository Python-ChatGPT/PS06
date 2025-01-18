import scrapy
import csv

class DivannewparseSpider(scrapy.Spider):
    name = "divannewparse"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        parsed_data = []
        for divan in divans:
            name = divan.css('div.lsooF span[itemprop=name]::text').get()
            price = int(divan.css('div.lsooF meta[itemprop=price]').attrib['content'])
            url = divan.css('div.lsooF a.qUioe').attrib['href']
            parsed_data.append([name, price, url])

            yield {
                'name': name,
                'price': price,
                'url': url
            }

        with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название товара', 'Цена', 'Ссылка на товар'])
            writer.writerows(parsed_data)
