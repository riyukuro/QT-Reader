import ui.ui_main as ui_main
import ui.ui_util
from PySide6 import QtCore, QtGui, QtWidgets

from importlib import import_module
from requests import get
from os import getcwd

cwd = getcwd()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.browseBtn.clicked.connect(self.browse_installed_sources)
        self.ui.topBar.hide()
        self.ui.backBtn.clicked.connect(self.back)

    def browse_installed_sources(self):
        if self.ui.backBtn.isVisible() is True: self.ui.backBtn.hide()
        """ Creates the Browse Page for installed sources. (Buttons link to the 'testing' method) """
        # Clears "dead" pages.
        for i in range(0, self.ui.stackedWidget.count()): self.ui.stackedWidget.widget(i).deleteLater()
        
        self.browse_sources_page = QtWidgets.QWidget()
        self.browse_sources_page.setObjectName(u'Browse Page')

        self.browse_ScrollArea_Layout = QtWidgets.QHBoxLayout(self.browse_sources_page)
        self.browse_ScrollArea_Layout.setContentsMargins(0, 0, 0, 0)
        self.browse_ScrollArea_Layout.setSpacing(0)
        self.browse_ScrollArea_Layout.setObjectName("Browse ScrollArea Layout")

        self.browse_ScrollArea = QtWidgets.QScrollArea(self.browse_sources_page)
        self.browse_ScrollArea.setWidgetResizable(True)
        self.browse_ScrollArea.setObjectName('Browse ScrollArea')

        self.browse_ScrollArea_contents = QtWidgets.QWidget()
        self.browse_ScrollArea_contents.setObjectName(u'Browse ScrollArea Contents')

        self.browse_ScrollArea_contents_Vlayout = QtWidgets.QVBoxLayout(self.browse_ScrollArea_contents)
        self.browse_ScrollArea_contents_Vlayout.setContentsMargins(0, 0, 0, 0)
        self.browse_ScrollArea_contents_Vlayout.setSpacing(0)
        self.browse_ScrollArea_contents_Vlayout.setObjectName('Browse ScrollArea Contents Layout')

        self.browse_button_frame = QtWidgets.QFrame(self.browse_ScrollArea_contents)
        self.browse_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.browse_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.browse_button_frame.setObjectName('Browse Button Frame')

        self.browse_button_frame_Vlayout = QtWidgets.QVBoxLayout(self.browse_button_frame)
        self.browse_button_frame_Vlayout.setObjectName('Browse Button Frame Layout')

        from util import generate_installed_sources
        for i in generate_installed_sources():
            self.buttonsHLayout = QtWidgets.QHBoxLayout()
            self.buttonsHLayout.setContentsMargins(0, 0, 0, 0)
            self.buttonsHLayout.setSpacing(0)

            # Source Title Button
                # Search

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(i['thumbnail']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.sourceButton = QtWidgets.QToolButton(self.browse_button_frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.sourceButton.sizePolicy().hasHeightForWidth())
            self.sourceButton.setSizePolicy(sizePolicy)
            self.sourceButton.setIcon(icon)
            self.sourceButton.setIconSize(QtCore.QSize(48, 48))
            self.sourceButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
            self.sourceButton.setAutoRaise(True)
            self.sourceButton.setText(i['source']) 
            self.sourceButton.setObjectName(i['source'])
            self.sourceButton.setProperty('use', 'search')
            self.sourceButton.clicked.connect(self.testing)
            self.buttonsHLayout.addWidget(self.sourceButton)

            # Latest Button

            self.latestButton = QtWidgets.QToolButton(self.browse_button_frame)
            self.latestButton.setAutoRaise(True)
            self.latestButton.setText('Latest')
            self.latestButton.setMinimumSize(QtCore.QSize(0, 55))
            self.latestButton.setObjectName(i['source'])
            self.latestButton.setProperty('use', 'latest')
            self.latestButton.clicked.connect(self.testing)
            self.buttonsHLayout.addWidget(self.latestButton, 0, QtCore.Qt.AlignRight)
            
            # Popular Button

            self.popularButton = QtWidgets.QToolButton(self.browse_button_frame)
            self.popularButton.setAutoRaise(True)
            self.popularButton.setText('Popular')
            self.popularButton.setMinimumSize(QtCore.QSize(0, 55))
            self.popularButton.setObjectName(i['source'])
            self.popularButton.setProperty('use', 'popular')
            self.popularButton.clicked.connect(self.testing)
            self.buttonsHLayout.addWidget(self.popularButton)

            self.browse_button_frame_Vlayout.addLayout(self.buttonsHLayout)

        self.browse_ScrollArea_contents_Vlayout.addWidget(self.browse_button_frame, 0, QtCore.Qt.AlignTop)
        self.browse_ScrollArea.setWidget(self.browse_ScrollArea_contents)
        self.browse_ScrollArea_Layout.addWidget(self.browse_ScrollArea)

        # Add page to StackedWidget, changes to page & changes window title.
        self.ui.stackedWidget.addWidget(self.browse_sources_page)
        page = self.ui.stackedWidget.findChild(QtWidgets.QWidget,'Browse Page')
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(page))
        self.setWindowTitle('Browse')

    def testing(self): # TODO Rename Method, Add Search, Check for performance issues.
        """ Handles fetching of Popular & Latest novels from sources for the generate_covers method """
        source_name = str(self.sender().objectName())
        source = import_module('sources.' + source_name)
        if self.sender().property('use') == 'popular': 
            self.browse_source(source.fetchPopular(), source_name)
            self.setWindowTitle(source_name + ' Popular')

        elif self.sender().property('use') == 'search':
            self.search(source_name)

        else: 
            self.browse_source(source.fetchLatest(), source_name)
            self.setWindowTitle(source_name + ' Latest')

    def browse_source(self, data, source):
        """ Generates the library layout page which generate_covers uses to add entries. """
        self.browse_library_page = QtWidgets.QWidget()
        self.browse_library_page.setObjectName('Library Page')

        self.browse_library_layout = QtWidgets.QHBoxLayout(self.browse_library_page)
        self.browse_library_layout.setContentsMargins(0, 0, 0, 0)
        self.browse_library_layout.setSpacing(0)

        self.browse_library_scrollArea = QtWidgets.QScrollArea(self.browse_library_page)
        self.browse_library_scrollArea.setObjectName('Library Scroll Area')
        self.browse_library_scrollArea.setWidgetResizable(True)

        self.widget = QtWidgets.QWidget(self.browse_library_scrollArea)
        self.widget.setMinimumHeight(50)

        layout = ui.ui_util.FlowLayout(self.widget)
        self.browse_library_scrollArea.setWidget(self.widget)
        self.browse_library_layout.addWidget(self.browse_library_scrollArea)

        self.ui.stackedWidget.addWidget(self.browse_library_page)
        page = self.ui.stackedWidget.findChild(QtWidgets.QWidget,'Library Page')
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(page))
        
        import textwrap as tw
        for i in data:
            QtCore.QCoreApplication.processEvents()
            generated_cover = QtWidgets.QToolButton()
            if len(i['cover']) > 1:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(get(i['cover']).content)
            else: pixmap = QtGui.QPixmap(f'{cwd}/res/no_cover.jpg')
            pixmap_rescale = pixmap.scaled(110, 150, QtCore.Qt.KeepAspectRatio) #120,170
            generated_cover.setIcon(QtGui.QIcon(pixmap_rescale))
            generated_cover.setIconSize(pixmap_rescale.rect().size())
            generated_cover.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            generated_cover.setStyleSheet('font-size: 11px;')
            generated_cover.setText(tw.fill(i['title'], 15)) #19
            generated_cover.setAutoRaise(True)
            generated_cover.setProperty('url', i['url'])
            generated_cover.setProperty('source', source)
            generated_cover.clicked.connect(self.novel_info)
            layout.addWidget(generated_cover)

        if self.ui.backBtn.isVisible() is False: self.ui.backBtn.show()

    def novel_info(self):
        """ Creates the Info page for the Novel. (Cover, Title, Description & Chapter List) """
        source = self.sender().property('source')
        data_import = import_module('sources.' + source)
        self.info_data = data_import.fetchDetails(self.sender().property('url'))

        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName('Info Page')

        self.info_vertical_layout = QtWidgets.QVBoxLayout(self.info_page)
        self.info_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.info_vertical_layout.setSpacing(0)

        self.info_pane_frame = QtWidgets.QFrame()
        self.info_pane_frame.setMaximumSize(16777215, 300)

        self.info_pane_layout = QtWidgets.QGridLayout(self.info_pane_frame)
        self.info_pane_layout.setSpacing(0)

        if len(self.info_data[0]['cover']) > 1:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(get(self.info_data[0]['cover']).content)
        else: pixmap = QtGui.QPixmap(f'{cwd}/res/no_cover.jpg')
        self.cover = QtWidgets.QLabel()
        self.cover.setPixmap(pixmap)
        self.cover.setMaximumSize(QtCore.QSize(190, 280))
        self.cover.setScaledContents(True)
        self.info_pane_layout.addWidget(self.cover, 0, 0, 3, 1)

        #self.author = QtWidgets.QLabel()
        #self.author.setText('Author Name')
        #self.author.setStyleSheet("font: 9pt;")
        #self.info_pane_layout.addWidget(self.author, 1, 1, 1, 1)

        self.title = QtWidgets.QLabel()
        self.title.setText(self.info_data[0]['title'])
        self.info_pane_layout.addWidget(self.title, 0, 1, 1, 1)

        self.desc = QtWidgets.QTextBrowser()
        self.desc.setText(self.info_data[0]['desc'])
        #self.desc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_pane_layout.addWidget(self.desc, 2, 1, 1, 2)

        self.bookmark = QtWidgets.QCheckBox()
        self.bookmark.setCheckable(True)
        self.bookmark.setMaximumSize(QtCore.QSize(48, 48))
        self.bookmark.setStyleSheet(f'QCheckBox::indicator:checked\n{{\nimage: url({cwd}/res/bookmark_white_48dp.svg);\n}}\nQCheckBox::indicator:unchecked\n{{\nimage: url({cwd}/res/bookmark_border_white_48dp.svg);\n}}')

        self.info_pane_layout.addWidget(self.bookmark, 0, 2, 1, 1)

        self.info_vertical_layout.addWidget(self.info_pane_frame)

        self.chapter_scroll = QtWidgets.QScrollArea(self.info_page)
        self.chapter_scroll.setWidgetResizable(True)
        
        self.chapter_scroll_contents = QtWidgets.QWidget()

        self.chapter_scroll_layout = QtWidgets.QVBoxLayout(self.chapter_scroll_contents)
        self.chapter_scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.chapter_scroll_layout.setSpacing(0)
        button_num = 0
        for i in self.info_data[1]:
            self.chapter = QtWidgets.QPushButton()
            self.chapter.setText(i['title'])
            self.chapter.setObjectName(str(button_num))
            self.chapter.setProperty('url', i['url'])
            self.chapter.setProperty('source', source)
            self.chapter.clicked.connect(self.novel_reader)
            self.chapter_scroll_layout.addWidget(self.chapter)
            button_num += 1

        self.chapter_scroll.setWidget(self.chapter_scroll_contents)
        
        self.info_vertical_layout.addWidget(self.chapter_scroll)

        if self.ui.backBtn.isVisible() is False: self.ui.backBtn.show()

        self.ui.stackedWidget.addWidget(self.info_page)
        page = self.ui.stackedWidget.findChild(QtWidgets.QWidget,'Info Page')
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(page))
        
    def novel_reader(self):
        source_name = self.sender().property('source')
        source = import_module('sources.' + source_name)
        url = self.sender().property('url')
        chapter_num = int(self.sender().objectName())

        contents = source.fetchChapter(url)

        self.novel_reader_page = QtWidgets.QWidget()
        self.novel_reader_page.setObjectName('Reader Page')

        self.page_layout = QtWidgets.QVBoxLayout(self.novel_reader_page)
        self.page_layout.setContentsMargins(0,0,0,0)
        self.page_layout.setSpacing(0)

        self.reader_page_topbar = QtWidgets.QFrame()
        self.reader_page_topbar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.reader_page_topbar_layout = QtWidgets.QHBoxLayout(self.reader_page_topbar)
        self.reader_page_topbar_layout.setSpacing(0)
        self.reader_page_topbar_layout.setContentsMargins(0, 0, 0, 0)

        self.prev = QtWidgets.QPushButton()
        self.prev.setText('Prev')
        self.prev.setProperty('num', chapter_num)
        self.prev.setProperty('source', source_name)
        self.prev.setProperty('direction', 'prev')
        self.prev.clicked.connect(self.chap)
        self.reader_page_topbar_layout.addWidget(self.prev)

        self.next = QtWidgets.QPushButton()
        self.next.setText('Next')
        self.next.setProperty('num', chapter_num)
        self.next.setProperty('source', source_name)
        self.next.setProperty('direction', 'next')
        self.next.clicked.connect(self.chap)
        self.reader_page_topbar_layout.addWidget(self.next)

        self.page_layout.addWidget(self.reader_page_topbar)

        self.reader = QtWidgets.QTextBrowser()
        self.reader.setText(str(contents))
        self.page_layout.addWidget(self.reader)

        if self.ui.backBtn.isVisible() is False: self.ui.backBtn.show()
        self.ui.topBar.show()
        
        self.ui.stackedWidget.addWidget(self.novel_reader_page)
        page = self.ui.stackedWidget.findChild(QtWidgets.QWidget,'Reader Page')
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(page))

    def chap(self):
        source_name = self.sender().property('source')
        source = import_module('sources.' + source_name)
        num = int(self.sender().property('num'))
        if self.sender().property('direction') == 'next': 
            num += 1
        else: 
            if num != 0: num -= 1
        self.next.setProperty('num', str(num))
        self.prev.setProperty('num', str(num))
        url = self.info_data[1][num]['url']
        self.reader.setText(str(source.fetchChapter(url)))
        return
    
    def back(self):
        current_page = self.ui.stackedWidget.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(current_page-1)
        self.ui.stackedWidget.widget(current_page).deleteLater()
        if self.ui.stackedWidget.currentIndex() < 1: self.ui.backBtn.hide()

    def search(self, source_name):
        self.search_page = QtWidgets.QWidget()
        self.search_page.setObjectName(u'Search Page')

        self.search_page_layout = QtWidgets.QVBoxLayout(self.search_page)
        self.search_page_layout.setSpacing(0)
        self.search_page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.searchBarFrame = QtWidgets.QFrame(self.search_page)
        self.searchBarFrame.setMaximumHeight(50)
        self.searchBarFrameLayout = QtWidgets.QHBoxLayout(self.searchBarFrame)

        self.searchBar = QtWidgets.QLineEdit(self.searchBarFrame)
        self.searchBarFrameLayout.addWidget(self.searchBar)

        self.searchButton = QtWidgets.QPushButton()
        self.searchButton.setText('Search')
        self.searchButton.setShortcut('enter')
        self.searchButton.clicked.connect(lambda: self.search_results(self.searchBar.text(), source_name))
        self.searchBarFrameLayout.addWidget(self.searchButton, 0, QtCore.Qt.AlignLeft)

        self.search_page_layout.addWidget(self.searchBarFrame)

        self.searchScrollArea = QtWidgets.QScrollArea(self.search_page)
        self.searchScrollArea.setWidgetResizable(True)
        self.searchScrollArea.setObjectName('Search Scroll Area')

        self.widget2 = QtWidgets.QWidget(self.searchScrollArea)
        self.widget2.setMinimumHeight(50)
        self.layout = ui.ui_util.FlowLayout(self.widget2)

        self.searchScrollArea.setWidget(self.widget2)
        self.search_page_layout.addWidget(self.searchScrollArea)

        self.ui.stackedWidget.addWidget(self.search_page)
        page = self.ui.stackedWidget.findChild(QtWidgets.QWidget,u'Search Page')
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(page))
        if self.ui.backBtn.isVisible() is False: self.ui.backBtn.show()

    def search_results(self, title, source_name):
        if self.layout.count() != 0: self.layout.__del__()

        from importlib import import_module
        source = import_module('sources.' + source_name)
        data = source.fetchSearch(str(title))

        import textwrap as tw
        for i in data:
            QtCore.QCoreApplication.processEvents()
            generated_cover = QtWidgets.QToolButton()
            if len(i['cover']) > 1:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(get(i['cover']).content)
            else: pixmap = QtGui.QPixmap(f'{cwd}/res/no_cover.jpg')
            pixmap_rescale = pixmap.scaled(110, 150, QtCore.Qt.KeepAspectRatio) #120,170
            generated_cover.setIcon(QtGui.QIcon(pixmap_rescale))
            generated_cover.setIconSize(pixmap_rescale.rect().size())
            generated_cover.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            generated_cover.setStyleSheet('font-size: 11px;')
            generated_cover.setText(tw.fill(i['title'], 15)) #19
            generated_cover.setAutoRaise(True)
            generated_cover.setProperty('url', i['url'])
            generated_cover.setProperty('source', source_name)
            generated_cover.clicked.connect(self.novel_info)
            self.layout.addWidget(generated_cover)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setPalette(ui.ui_util.palettes.dark_palette)
    window = MainWindow()
    window.setWindowTitle('LN Reader')
    sys.exit(app.exec_())