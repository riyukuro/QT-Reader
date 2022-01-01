from sources.lib import madara #pylint: disable=import-error

base_url = 'https://boxnovel.com'

def fetchPopular(): 
    popular_url = base_url + '/novel/?m_orderby=trending'
    popular_selector = 'div.col-xs-12.col-md-6'
    return madara.fetchPopular(popular_url, popular_selector)

def fetchLatest(): 
    latest_url = base_url + '/?m_orderby=latest'
    latest_selector = 'div.col-xs-12.col-md-6'
    return madara.fetchLatest(latest_url, latest_selector)

def fetchSearch(search): 
    search_url = base_url + f'/?s={search}&post_type=wp-manga'
    return madara.fetchSearch(search_url, None)

def fetchDetails(novel_url): 
    return madara.fetchDetails(novel_url)

def fetchChapter(chapter_url):
    return madara.fetchChapter(chapter_url)