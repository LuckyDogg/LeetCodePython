import
def get_commodity(start_url):
    jd_data=requests.get(start_url)
    jd_data.encoding='utf8'
    time.sleep(1)
    soup=BeautifulSoup(jd_data.text,"lxml")
    #价格
    goods_prices=soup.select(".gl-i-wrap strong i")
    #名称
    goods_titles=soup.select(".p-name a em")
    #商品链接
    goods_urls=soup.select(".p-name a")
    for goods_title,goods_price,goods_url,goods_comment,goods_img in zip(goods_titles,goods_prices,goods_urls):
        data={
            'goods_title':goods_title.get_text(),
            'goods_price':goods_price.get_text(),
            'goods_url':goods_url.get('href'),
        }
