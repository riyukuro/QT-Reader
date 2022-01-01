from sources.lib import madara #pylint: disable=import-error

base_url = 'https://vipnovel.com'

def fetchPopular(): 
    popular_url = base_url + '/vipnovel/?m_orderby=trending'
    return madara.fetchPopular(popular_url, None)

def fetchLatest(): 
    latest_url = base_url + '/?m_orderby=latest'
    return madara.fetchLatest(latest_url, None)

def fetchSearch(search): 
    search_url = base_url + f'/?s={search}&post_type=wp-manga'
    return madara.fetchSearch(search_url, None)

def fetchDetails(novel_url): 
    return madara.fetchDetails(novel_url)

def fetchChapter(chapter_url):
    return madara.fetchChapter(chapter_url)