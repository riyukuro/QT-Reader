from sources.lib import madara #pylint: disable=import-error
from bs4 import BeautifulSoup
import requests as r
import re

base_url = 'https://woopread.com'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def fetchPopular(): 
    popular_url = base_url + '/novellist/?m_orderby=trending'
    return madara.fetchPopular(popular_url, None)

def fetchLatest(): 
    latest_url = base_url + '/?m_orderby=latest'
    latest_selector = 'div.col-6.col-md-3.badge-pos-2'
    return madara.fetchLatest(latest_url, latest_selector)

def fetchSearch(search): 
    search_url = base_url + f'/?s={search}&post_type=wp-manga'
    return madara.fetchSearch(search_url, None)

def fetchDetails(novel_url):
    try:
        request = r.get(novel_url, headers=header)
    except r.exceptions.RequestException as e:
        return e

    details = BeautifulSoup(request.text, 'html.parser')
    title = details.select_one('div.post-title').get_text().replace('NEW', '').replace('HOT', '').lstrip().rstrip()
    cover = details.select_one('.summary_image img')['src']
    desc = details.select_one('div.summary__content.show-more').findAll('p')#.getText()

    detail_result = [{'title': title, 'cover': str(cover), 'desc': desc}]

    novel_id = details.select_one('input.rating-post-id')['value']

    # FetchChapterList
    
    data = {"action": "manga_get_chapters", "manga": novel_id}
    chapter_ajax = r.post(base_url + '/wp-admin/admin-ajax.php', data=data, headers=header)
    chapter_list = BeautifulSoup(chapter_ajax.text, 'html.parser').select('li.wp-manga-chapter a')
    chapter_list_results = list()

    for i in reversed(chapter_list):
        title = i.text.strip()
        chapter_list_results.append({'title': title, 'url': i['href']})
    
    detail_result.append(chapter_list_results)

    return detail_result

def fetchChapter(chapter_url):
    return madara.fetchChapter(chapter_url)