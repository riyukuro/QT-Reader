def generate_installed_sources():
    import os
    sources = []
    sources_dir = os.path.dirname(os.path.abspath(__file__)) + '/sources'

    for entry in os.listdir(sources_dir):
        if '.py' in entry:
            x = {'source': entry.strip('.py'), 'thumbnail': sources_dir + '/thumbnails/' + entry.replace('.py', '.png')}
            sources.append(x)
    return sources

from PySide6.QtWidgets import QErrorMessage
def error_handler(e):
    error_dialogue = QErrorMessage()
    error_dialogue.showMessage(e)
    error_dialogue.setWindowTitle('Error occurred')
    error_dialogue.exec()