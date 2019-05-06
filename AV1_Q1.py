import scrapy
from scrapy.utils.response import open_in_browser

class UolSpider(scrapy.Spider):

    name = 'Uol Dólar'
    start_urls = {'https://www.uol.com.br/'}

    def parse(self, response):
        #open_in_browser(response)
        cotacao = response.css('.currency_quote__down')
        for dolar in cotacao:
            print('\n >> A cotação atual do dólar é: ' + str(dolar.css('::text').extract_first()))