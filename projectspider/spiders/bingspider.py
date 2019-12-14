#Notes:
# To run the command >> scrapy crawl ispider01 -a "urls=http://quotes.toscrape.com/page/2/, http://quotes.toscrape.com/page/3/" -o dynaspider.json
# Install user agents on the machine/server from https://pypi.org/project/scrapy-user-agents/
# Add the following in the settings.py, also require to enable useragents for Google or any search engine.
# Enable the DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
# }
import scrapy
import logging

from ..items import ProjectspiderItem

logger = logging.getLogger('bingspiderlogger')


class BingSpider(scrapy.Spider):
    name = "bingspider"
    start_urls = []

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls.split(',')
        # self.logger.info(self.start_urls)
        # QuotesSpider.rules=(Rule(LxmlLinkExtractor(allow=(),unique=True), callback='parse_obj', follow=True),)
        super(BingSpider, self).__init__(*args, **kwargs)
        logger.info("Successfully passed the url!")

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        items = ProjectspiderItem()
        tags = response.css('div.b_content')


        for i in tags:
            # title = response.xpath('span.S3Uucc').getall(),
            title = response.xpath('//span[@class="h2"]/text()').getall(),
            desc = response.xpath('//span[@class="p"]/text()').getall(),
            url = response.xpath('//span[@class="cite"]/href').getall(),
            logger.info("Successfully captured the page elements")

            items['title'] = title,
            items['desc'] = desc,
            items['url'] = url,

        yield items
        logger.info("Successfully sent data to item containers.")
        next_page = response.css('a.sb_bp :: attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            logger.info("Successfully going to next page")
