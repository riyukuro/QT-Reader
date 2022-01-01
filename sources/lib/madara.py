# CMS: Madara, Version: 0.1

from bs4 import BeautifulSoup
import requests as r

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def fetchPopular(popular_url, popular_selector):
    popular_results = list()

    try:
        request = r.get(popular_url, headers=header)
    except r.exceptions.RequestException as e:
        return e
    popular = BeautifulSoup(request.text, 'html.parser')

    if popular_selector is None:
        popular_selector = 'div.col-12.col-md-6'
    
    for i in popular.select(popular_selector):
        popular_results.append({'title': i.div.a['title'], 'url': i.div.a['href'], 'cover': i.div.a.img['src']})
    
    return popular_results

def fetchLatest(latest_url, latest_selector):
    latest_results = list()

    try:
        request = r.get(latest_url, headers=header)
    except r.exceptions.RequestException as e:
        return e
    latest = BeautifulSoup(request.text, 'html.parser')

    if latest_selector is None:
        latest_selector = 'div.col-12.col-md-6'

    for i in latest.select(latest_selector):
        latest_results.append({'title': i.div.a['title'], 'url': i.div.a['href'], 'cover': i.div.a.img['src']})

    return latest_results

def fetchSearch(search_url, search_selector):
    search_results = list()
    if search_selector is None:
        search_selector = 'div.c-tabs-item__content'

    try:
        request = r.get(search_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    search = BeautifulSoup(request.text, 'html.parser')

    for i in search.select('div.c-tabs-item__content:nth-child(n)'):
        search_results.append({'title': i.div.div.a['title'], 'url': i.div.div.a['href'], 'cover': i.div.div.a.img['src']})
    return search_results
    
def fetchDetails(novel_url):
    
    try:
        request = r.get(novel_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    details = BeautifulSoup(request.text, 'html.parser')
    title = details.select_one('h3').get_text().replace('NEW', '').replace('HOT', '').lstrip().rstrip()
    cover = details.select_one('.summary_image img')['src']
    desc = details.select_one('p').getText()

    detail_result = [{'title': title, 'cover': str(cover), 'desc': desc}]

    # FetchChapterList
    chapter_list = details.select('ul.main li.wp-manga-chapter a')
    chapter_list_results = list()

    for i in reversed(chapter_list):
        chapter_list_results.append({'title': i.text.strip(), 'url': i['href']})
    
    detail_result.append(chapter_list_results)

    return detail_result

def fetchChapter(chapter_url):
    try:
        request = r.get(chapter_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    chapter_body = BeautifulSoup(request.text, 'html5lib').select_one('div.text-left').findAll('p')
    chapter = ''.join(str(x) + '\n' for x in chapter_body)

    return chapter