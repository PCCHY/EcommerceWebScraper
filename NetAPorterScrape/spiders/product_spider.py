import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'

    def start_requests(self):
        urls = [
            'https://www.net-a-porter.com/en-in/shop/clothing/tops',
            'https://www.net-a-porter.com/en-in/shop/shoes'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # List of All the products
        productlist = response.css("div.ProductGrid52 a")

        for product in productlist:
            relativelink = product.css('::attr("href")').get()
            if self.isDiscount(product):
                original_price = float(product.xpath('//s[@class="PriceWithSchema9__wasPrice"]/text()').get()[1:])
                sale_price = float(product.xpath('//span[@class="PriceWithSchema9__value"]/span/@content').get())
            else:
                original_price = float(product.xpath('//span[@class="PriceWithSchema9__value"]/span/@content').get())
                sale_price = float(product.xpath('//span[@class="PriceWithSchema9__value"]/span/@content').get())

            productDetails = {
                'name': product.css('span.ProductItem24__name::text').get(),
                'brand': product.css('span.ProductItem24__designer::text').get(),
                'original_price': original_price,
                'sale_price': sale_price,
                'image_url': product.xpath('//img[@class="Image18__image"]/@src').get(),
                'product_page_url': response.urljoin(relativelink),
                'product_category': self.urlcategory(response.request.url),
            }
            if productDetails['name'] is not None:
                yield productDetails

        # Scrape the Site upto 25 Pages
        nextPage = response.css('a.Pagination7__next::attr("href")').get()
        if nextPage is not None:
            num = int(nextPage.split("=")[-1])
            if num < 26:
                yield response.follow(nextPage, callback=self.parse)

    def urlcategory(self, url):
        # Function to extract category from URL provided
        # Input: URL
        # Output: Url Category
        if 'shoes' in url:
            category = 'footwear'
        elif 'tops' in url:
            category = 'topwear'
        return category

    def isDiscount(self, product):
        # Function to check if product have discount
        # Input: Product details
        # Output: True if product have discount else false
        originalPrice = product.xpath('//s[@class="PriceWithSchema9__wasPrice"]/text()').get()
        if originalPrice is None:
            return False
        return True
