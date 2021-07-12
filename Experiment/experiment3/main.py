from bs4 import BeautifulSoup
import urllib.request

def get_soup(url):
    res = urllib.request.urlopen(url).read()
    res = res.decode("utf-8")
    soup = BeautifulSoup(res, "html.parser")  # 解析网页
    return soup

def get_information(soup, url):
    dict = {}
    title = soup.select_one('.main-title')
    if (title == None):
        return dict
    dict['title'] = title.text
    time_source = soup.select_one('.date-source')
    time = time_source.find_all('span', {'class': 'date'})[0].text
    dict['site'] = time_source.find_all('a', {'class': 'source'})[0].text
    dict['time'] = time
    article = soup.select('.article')[0]
    content = []
    for p in article.select('p'):
        if p.select('font'):
            content.append(p.select('font')[0].text)
        else:
            content.append(p.text)
    content = ' '.join(content)  # 生成器写法
    # ' '.join(content)  #将其合并为字符串
    dict['content'] = content[0:100]  # 新闻详情
    # 取出责任编辑
    if soup.select_one('.show_author') != None:
        editor = soup.select_one('.show_author').text.lstrip('责任编辑：')  # 并从左边将责任编辑：移除
        print(editor)
        dict['editor'] = editor
    return dict

new_urls = set()  # 存放未访问url set集合
url = 'http://news.sina.com.cn/china/'
web_data = urllib.request.urlopen(url).read()
web_data = web_data.decode("utf-8")
# print(web_data)
soup = BeautifulSoup(web_data, "html.parser")  # 解析网页
print(soup)

for news in soup.select('.news-2'):
    print('---------------')
    for newschild in news.select('a'):
        newstitle = newschild.text  # 新闻标题
        news_href = newschild['href']  # 新闻链接
        new_urls.add(news_href)

content = []
while 1:
    if (not new_urls):  # 判断是否为空集合，如果空集合则终止循环
        break
    else:
        # 从url集合中得到要访问的url
        url = new_urls.pop()
        soup = get_soup(url)  # 得到soup
        dict = get_information(soup, url)
        content.append(dict)
        print(dict)
