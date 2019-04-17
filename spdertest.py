import urllib
import json
def jd_price(url):
        sku = url.split('/')[-1].strip(".html")
        price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + sku
        response = urllib.urlopen(price_url)
        content = response.read()
        result = json.loads(content)
        record = resuylt[0]
        return record['p']
if __name__=="__main__":
        jd_price("https://item.jd.com/5089225.html")
