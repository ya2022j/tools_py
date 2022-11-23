

# python3   update_nhk_news_Server.py

import scrapy
from scrapy_splash import SplashRequest
from urllib import parse
import json

big_list = []
nhk_news_file = "/home/mk_m/device/nhk_news.json"

def writeinto_jsonfile(filename, list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)



class Spider(scrapy.Spider):
    name = ''
    allowed_domains = []
    start_urls = ['https://nikkei225jp.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait':1}, endpoint='render.html')

    def parse(self, response):
        title = response.xpath('//*[@id="newsDIV"]/ul/li/a/text()').extract()
        url = response.xpath('//*[@id="newsDIV"]/ul/li/a/@href').extract()
        f_url = [parse.unquote("".join(x.split("//jump.nikkei225jp.com/j.php?URL="))) for x in url]
        time_ = response.xpath('//*[@id="newsDIV"]/ul/li/tt/text()').extract()
        print(title,url,f_url,time_)

        for i1, i2, i3 in zip(title, f_url, time_):
            one_result = {}
            one_result["time_html"] = '<div class="m-miR13_time">{0}</div>'.format(i3)
            one_result[
                "title_html"] = '<a href="{0}" style="color:#333;"><h3 class="m-miR13_text">{1}</h3></a></li>'.format(
                i2, i1)
            print(one_result)
            big_list.append(one_result)



        writeinto_jsonfile(nhk_news_file, big_list)
        print(__file__, "----->OK")