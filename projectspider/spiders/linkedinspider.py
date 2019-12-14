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

logger = logging.getLogger('linkedinspiderlogger')


class LinkedinSpider(scrapy.Spider):
    name = "linkedinspider"
    start_urls = []

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls.split(',')
        # self.logger.info(self.start_urls)
        # QuotesSpider.rules=(Rule(LxmlLinkExtractor(allow=(),unique=True), callback='parse_obj', follow=True),)
        super(LinkedinSpider, self).__init__(*args, **kwargs)
        logger.info("Successfully passed the url!")

    def parse(self, response):
        items = ProjectspiderItem()
        tags = response.css('div.g')
        self.logger.info('Parse function called on %s', response.url)

        for i in tags:
            # title = response.xpath('span.S3Uucc').getall(),
            title = response.xpath('//span[@class="S3Uucc"]/text()').getall(),
            desc = response.xpath('//span[@class="st"]/text()').getall(),
            url = response.xpath('//span[@class="bc"]/href').getall(),
            logger.info("Successfully captured the page elements")

            items['title'] = title,
            items['desc'] = desc,
            items['url'] = url,

        yield items
        logger.info("Successfully sent data to item containers.")
        next_page = response.css('a.pn ::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            logger.info("Successfully going to next page")
