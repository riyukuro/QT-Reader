from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CW_horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.CW_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.CW_horizontalLayout.setSpacing(0)
        self.CW_horizontalLayout.setObjectName("CW_horizontalLayout")
        self.SideNav = QtWidgets.QFrame(self.centralwidget)
        self.SideNav.setMaximumSize(QtCore.QSize(70, 16777215))
        self.SideNav.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SideNav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideNav.setStyleSheet('background-color: rgb(26, 26, 26);')
        self.SideNav.setObjectName("SideNav")
        self.SideNav_Layout = QtWidgets.QVBoxLayout(self.SideNav)
        self.SideNav_Layout.setContentsMargins(0, 0, 0, 0)
        self.SideNav_Layout.setSpacing(0)
        self.SideNav_Layout.setObjectName("SideNav_Layout")
        self.Buttons_sidenav = QtWidgets.QFrame(self.SideNav)
        self.Buttons_sidenav.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Buttons_sidenav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Buttons_sidenav.setObjectName("Buttons_sidenav")
        self.SN_BTN_verticalLayout = QtWidgets.QVBoxLayout(self.Buttons_sidenav)
        self.SN_BTN_verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.SN_BTN_verticalLayout.setSpacing(10)
        self.SN_BTN_verticalLayout.setObjectName("SN_BTN_verticalLayout")
        self.LibraryBtn = QtWidgets.QToolButton(self.Buttons_sidenav)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/library_books_white_48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LibraryBtn.setIcon(icon)
        self.LibraryBtn.setIconSize(QtCore.QSize(24, 24))
        self.LibraryBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.LibraryBtn.setAutoRaise(True) ##
        #self.LibraryBtn.setStyleSheet('')
        self.LibraryBtn.setObjectName("LibraryBtn")
        self.SN_BTN_verticalLayout.addWidget(self.LibraryBtn)
        self.BrowseBtn = QtWidgets.QToolButton(self.Buttons_sidenav)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./res/explore_white_48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BrowseBtn.setIcon(icon1)
        self.BrowseBtn.setIconSize(QtCore.QSize(24, 24))
        self.BrowseBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.BrowseBtn.setAutoRaise(True) ##
        self.BrowseBtn.setObjectName("BrowseBtn")
        self.SN_BTN_verticalLayout.addWidget(self.BrowseBtn)
        self.SourcesBtn = QtWidgets.QToolButton(self.Buttons_sidenav)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./res/settings_white_48dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SourcesBtn.setIcon(icon2)  
        self.SourcesBtn.setIconSize(QtCore.QSize(24, 24))
        self.SourcesBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.SourcesBtn.setAutoRaise(True) ##
        self.SourcesBtn.setObjectName("SourcesBtn")
        self.SN_BTN_verticalLayout.addWidget(self.SourcesBtn)
        self.SettingsBtn = QtWidgets.QToolButton(self.Buttons_sidenav)
        self.SettingsBtn.setIcon(icon2)
        self.SettingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.SettingsBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.SettingsBtn.setAutoRaise(True) ##
        self.SettingsBtn.setObjectName("SettingsBtn")
        self.SN_BTN_verticalLayout.addWidget(self.SettingsBtn)
        self.SideNav_Layout.addWidget(self.Buttons_sidenav, 0, QtCore.Qt.AlignTop)
        self.CW_horizontalLayout.addWidget(self.SideNav)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.Content_verticalLayout = QtWidgets.QVBoxLayout(self.Content)
        self.Content_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Content_verticalLayout.setSpacing(0)
        self.Content_verticalLayout.setObjectName("Content_verticalLayout")
        self.StackedWidget = QtWidgets.QStackedWidget(self.Content)
        self.StackedWidget.setObjectName("StackedWidget")
        self.Content_verticalLayout.addWidget(self.StackedWidget)
        self.CW_horizontalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LibraryBtn.setText(_translate("MainWindow", "Library"))
        self.LibraryBtn.setShortcut(_translate("MainWindow", "Esc"))
        self.BrowseBtn.setText(_translate("MainWindow", "Browse"))
        self.BrowseBtn.setShortcut(_translate("MainWindow", "Esc"))
        self.SourcesBtn.setText(_translate("MainWindow", "Sources"))
        self.SourcesBtn.setShortcut(_translate("MainWindow", "Esc"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.SettingsBtn.setShortcut(_translate("MainWindow", "Esc"))