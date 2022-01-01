from bs4 import BeautifulSoup
import requests as r

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
base_url = "https://novelfull.com"

def fetchPopular():
    popular_url = base_url + '/ajax-search?type=hot'

    try:
        request = r.get(popular_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    popular = BeautifulSoup(request.text, 'html.parser')
    popular_results = list()

    for i in popular.select('div.item'):
        popular_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': base_url + i.img['src']})
    return popular_results

def fetchLatest(): #No Covers
    latest_url = base_url + '/ajax-search?type=latest'
    try:
        request = r.get(latest_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    latest = BeautifulSoup(request.text, 'html.parser')
    latest_results = list()

    for i in latest.select('div.row'):
        latest_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': ''})
    return latest_results

def fetchSearch(novel_name):
    search_url = base_url + "/search?keyword="
    try:
        request = r.get(search_url + novel_name, headers=header)
    except r.exceptions.RequestException as e:
        return e
    search = BeautifulSoup(request.text, 'html.parser')
    search_results = list()
        
    for i in search.select('.archive > div:nth-child(1) > div.row'):
        search_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': base_url + i.img['src']})
    return search_results

def fetchDetails(novel_url):
    try:
        request = r.get(novel_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    novel = BeautifulSoup(request.text, 'html.parser')
    # Novel Details
    novel_title = novel.find('div', 'col-xs-12 col-sm-8 col-md-8 desc').h3.get_text()
    novel_cover = novel.find('div', 'book').img['src']
    novel_desc = novel.find('div', 'desc-text').get_text()
    details = [{'title': novel_title, 'cover': base_url + str(novel_cover), 'desc': novel_desc}]
    
    # Chapter List
    novelId = novel.find('div', id='rating')['data-novel-id']
    try:
        request = r.get(f'{base_url}/ajax-chapter-option?novelId={novelId}', headers=header)
    except r.exceptions.RequestException as e:
        return e
    
    chapter_list = BeautifulSoup(request.text, 'html.parser')
    chapter_list_results = list()
    chapter_id = 0

    for i in chapter_list.findAll('option'):
        chapter_list_results.append({'id': chapter_id, 'title': i.text, 'url': base_url + i['value']})
        chapter_id += 1
    
    details.append(chapter_list_results)

    return details

def fetchChapter(chapter_url):
    try:
        request = r.get(chapter_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    chapter_body = BeautifulSoup(request.text, 'html5lib').find('div', id='chapter-content').findAll('p')
    chapter = ''.join(str(x) + '\n' for x in chapter_body)
    return chapter