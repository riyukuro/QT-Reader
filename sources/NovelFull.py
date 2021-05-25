from bs4 import BeautifulSoup
import requests

#header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
base_url = "https://novelfull.com"

def fetch_popular():
    popular_url = base_url + '/ajax-search?type=hot'
    popular = BeautifulSoup(requests.get(popular_url).text, 'html.parser')
    popular_results = list()

    for i in popular.select('div.item'):
        popular_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': base_url + i.img['src']})
    return(popular_results)

def fetch_latest(): #No Covers
    latest_url = base_url + '/ajax-search?type=latest'
    latest = BeautifulSoup(requests.get(latest_url).text, 'html.parser')
    latest_results = list()

    for i in latest.select('div.row'):
        latest_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': ''})
    return(latest_results)

def fetch_search(novel_name):
    search_url = base_url + "/search?keyword="
    search = BeautifulSoup(requests.get(search_url + novel_name).text, 'html.parser')
    search_results = list()
        
    for i in search.select('.archive > div:nth-child(1) > div.row'):
        search_results.append({'title': i.a['title'], 'url': base_url + i.a['href'], 'cover': base_url + i.img['src']})
    return(search_results)

def fetch_novel_details(novel_url):
    novel = BeautifulSoup(requests.get(novel_url).text, 'html.parser')
    # Novel Details
    novel_title = novel.find('div', 'col-xs-12 col-sm-8 col-md-8 desc').h3.get_text()
    novel_cover = novel.find('div', 'book').img['src']
    novel_desc = novel.find('div', 'desc-text').get_text()
    details = [{'title': novel_title, 'cover': base_url + str(novel_cover), 'desc': novel_desc}]
    
    # Chapter List
    novelId = novel.find('div', id='rating')['data-novel-id']
    chapter_list = BeautifulSoup(requests.get(f'{base_url}/ajax-chapter-option?novelId={novelId}').text, 'html.parser')
    chapter_list_results = list()
    chapter_id = 0

    for i in chapter_list.findAll('option'):
        chapter_list_results.append({'id': chapter_id, 'title': i.text, 'url': base_url + i['value']})
        chapter_id += 1
    
    details.append(chapter_list_results)

    return details

def fetch_chapter_contents(chapter_url):
    chapter_body = BeautifulSoup(requests.get(chapter_url).text, 'html5lib').find('div', id='chapter-content')
    for strip in chapter_body(['script', 'ins']):
        strip.extract()

    return chapter_body
