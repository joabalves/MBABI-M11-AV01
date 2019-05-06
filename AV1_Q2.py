import scrapy
from scrapy.utils.response import open_in_browser

class MercadoLivreSpider(scrapy.Spider):

    name = 'Mercado Livre'
    produto = 'notebook'

    start_urls = {'https://lista.mercadolivre.com.br/{}'.format(produto)}
    
    def parse(self, response):
        #open_in_browser(response)
        produtos = response.css('.item__info')
        
        for produto in produtos:
            preco = produto.css('.price__fraction')
            descricao = produto.css('.main-title')

            print('Produto: '+str(descricao.css('::text').extract_first()))
            print('Valor: R$'+str(preco.css('::text').extract_first()))