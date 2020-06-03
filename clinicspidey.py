import scrapy
from ..items import FinalclinicItem
#imported the time module so that the hco would not kick me out. set the seconds to 10
import time

#this is to locate the hco website. you would have to reenter the number next to county and change that
# according to the county that it is assigned ie LA=19 and YUBA=58. Then change the number next to range if you want
#otherwise defautl it to 110 since LA is the biggest count
class QuoteSpider(scrapy.Spider):
    name = 'cli'
    start_urls = ['https://www.healthcareoptions.dhcs.ca.gov/choose/find-provider?tab=location&program=MEDI_CAL&provider_type=Medical%20Clinic&'
                  'option=county&county=58&page={}'.format(i) for i in range(0,3)]
    time.sleep(10)

    #this section identfies the pcp,plan,npi,and hco code by html
    def parse(self,response):
        items = FinalclinicItem()
        alldivquotes = response.css('div.provider')

        #used inspector gadget to locate the html info on the hco site. this is specific to Doctors ONLY
        for quotes in alldivquotes:
            pcp = quotes.css('.provider-name::text').extract()
            plan = quotes.css('.accepted-plan::text').extract()
            hcocode = quotes.css('.provider-detail-row:nth-child(4) .value::text').extract()
            npi = quotes.css('.provider-detail-row~ .provider-detail-row+ .provider-detail-row .value::text').extract()

            items['pcp'] = pcp
            items['plan'] = plan
            items['hcocode'] = hcocode
            items['npi'] = npi

            yield items





