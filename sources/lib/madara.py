from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def fetch_popular(base_url):
    popular_results = list()
    for i in range(3):
        popular_url = base_url + f'/novel/page/{str(i)}/?m_orderby=trending'
        popular = BeautifulSoup(requests.get(popular_url, headers=header).text, 'html.parser')
        
        for i in popular.select('div.page-listing-item:nth-child(n) > div > div > div'):
            popular_results.append({'title': i.div.a['title'], 'url': i.div.a['href'], 'cover': i.div.a.img['src']})
    return popular_results

def fetch_latest(base_url):
    latest_url = base_url + '/page/'
    latest_results = list()
    for page in range(3):
        latest = BeautifulSoup(requests.get(latest_url + str(page), headers=header).text, 'html.parser')
        
        for i in latest.select('div.page-listing-item:nth-child(n) > div > div > div'):
            latest_results.append({'title': i.div.a['title'], 'url': i.div.a['href'], 'cover': i.div.a.img['src']})
    
    return latest_results

def fetch_search(base_url, novel_name):
    search_url = base_url + f"/?s={novel_name}&post_type=wp-manga"
    search = BeautifulSoup(requests.get(search_url, headers=header).text, 'html.parser')
    search_results = list()
        
    for i in search.select('div.c-tabs-item__content:nth-child(n)'):
        search_results.append({'title': i.div.div.a['title'], 'url': i.div.div.a['href'], 'cover': i.div.div.a.img['src']})
    return search_results

def fetch_novel_details(novel_url):
    novel = BeautifulSoup(requests.get(novel_url, headers=header).text, 'html.parser')

    # Novel Details

    novel_title = novel.select_one('h3').get_text().replace('NEW', '').replace('HOT', '').lstrip().rstrip()
    novel_cover = novel.select_one('.summary_image img')['src']
    #novel_desc = novel.select_one('#editdescription').getText()
    novel_desc = novel.select_one('p').getText()
    details = [{'title': novel_title, 'cover': str(novel_cover), 'desc': novel_desc}]

    # Chapter List

    chapter_list = novel.select('ul.main li.wp-manga-chapter a')
    chapter_list_results = list()

    for i in reversed(chapter_list):
        chapter_list_results.append({'title': i.text.strip(), 'url': i['href']})
    
    details.append(chapter_list_results)

    return details

def fetch_chapter_contents(chapter_url):
    chapter_body = BeautifulSoup(requests.get(chapter_url, headers=header).text, 'html5lib').select_one('div.text-left').findAll('p')
    chapter = ''.join(str(x) + '\n' for x in chapter_body)

    return chapter