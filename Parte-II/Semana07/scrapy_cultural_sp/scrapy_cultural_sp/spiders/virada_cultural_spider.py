def parse(self, response):
    body_sel = Selector(response)
    urls_cidade = body_sel.xpath("//div[@class='list-cities']//ul//li//a/@href").extract()

    for url in urls_cidade:
        yield Request(url, self.parse_atracao)