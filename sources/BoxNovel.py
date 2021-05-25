from sources.lib import madara

base_url = 'https://boxnovel.com'

def fetch_popular(): return madara.fetch_popular(base_url)

def fetch_latest(): return madara.fetch_latest(base_url)

def fetch_search(search): return madara.fetch_search(base_url, search)

def fetch_novel_details(novel_url): return madara.fetch_novel_details(novel_url)

def fetch_chapter_contents(chapter_url): return madara.fetch_chapter_contents(chapter_url)