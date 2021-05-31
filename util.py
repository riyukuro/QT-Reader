def generate_installed_sources():
    import os
    sources = []
    dir = os.getcwd() + '/sources'

    for entry in os.listdir(dir):
        if '.py' in entry:
            x = {'source': entry.strip('.py'), 'thumbnail': dir + '/thumbnails/' + entry.replace('.py', '.png')}
            sources.append(x)
    return sources