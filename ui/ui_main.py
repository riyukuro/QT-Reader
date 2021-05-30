# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import res.ui_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(621, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CW_horizontalLayout = QHBoxLayout(self.centralwidget)
        self.CW_horizontalLayout.setSpacing(0)
        self.CW_horizontalLayout.setObjectName(u"CW_horizontalLayout")
        self.CW_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideNav = QFrame(self.centralwidget)
        self.sideNav.setObjectName(u"sideNav")
        self.sideNav.setMaximumSize(QSize(70, 16777215))
        self.sideNav.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.sideNav.setFrameShape(QFrame.NoFrame)
        self.sideNav.setFrameShadow(QFrame.Raised)
        self.SideNav_Layout = QVBoxLayout(self.sideNav)
        self.SideNav_Layout.setSpacing(0)
        self.SideNav_Layout.setObjectName(u"SideNav_Layout")
        self.SideNav_Layout.setContentsMargins(0, 10, 0, 10)
        self.buttons_SideNav = QFrame(self.sideNav)
        self.buttons_SideNav.setObjectName(u"buttons_SideNav")
        self.buttons_SideNav.setFrameShape(QFrame.NoFrame)
        self.buttons_SideNav.setFrameShadow(QFrame.Raised)
        self.SN_BTN_verticalLayout = QVBoxLayout(self.buttons_SideNav)
        self.SN_BTN_verticalLayout.setSpacing(10)
        self.SN_BTN_verticalLayout.setObjectName(u"SN_BTN_verticalLayout")
        self.SN_BTN_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.libraryBtn = QToolButton(self.buttons_SideNav)
        self.libraryBtn.setObjectName(u"libraryBtn")
        self.libraryBtn.setMinimumSize(QSize(70, 0))
        icon = QIcon()
        icon.addFile(u":/sidebar-dark/library_books_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.libraryBtn.setIcon(icon)
        self.libraryBtn.setIconSize(QSize(24, 24))
        self.libraryBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.libraryBtn.setAutoRaise(True)

        self.SN_BTN_verticalLayout.addWidget(self.libraryBtn)

        self.browseBtn = QToolButton(self.buttons_SideNav)
        self.browseBtn.setObjectName(u"browseBtn")
        self.browseBtn.setMinimumSize(QSize(70, 0))
        icon1 = QIcon()
        icon1.addFile(u":/sidebar-dark/explore_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browseBtn.setIcon(icon1)
        self.browseBtn.setIconSize(QSize(24, 24))
        self.browseBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.browseBtn.setAutoRaise(True)

        self.SN_BTN_verticalLayout.addWidget(self.browseBtn)

        self.sourcesBtn = QToolButton(self.buttons_SideNav)
        self.sourcesBtn.setObjectName(u"sourcesBtn")
        self.sourcesBtn.setMinimumSize(QSize(70, 0))
        self.sourcesBtn.setIcon(icon1)
        self.sourcesBtn.setIconSize(QSize(24, 24))
        self.sourcesBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.sourcesBtn.setAutoRaise(True)

        self.SN_BTN_verticalLayout.addWidget(self.sourcesBtn)

        self.settingsBtn = QToolButton(self.buttons_SideNav)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(70, 0))
        icon2 = QIcon()
        icon2.addFile(u":/sidebar-dark/settings_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QSize(24, 24))
        self.settingsBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settingsBtn.setAutoRaise(True)

        self.SN_BTN_verticalLayout.addWidget(self.settingsBtn)


        self.SideNav_Layout.addWidget(self.buttons_SideNav, 0, Qt.AlignTop)

        self.backBtn = QToolButton(self.sideNav)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(70, 0))
        icon3 = QIcon()
        icon3.addFile(u":/topBar/arrow_back_white_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon3)
        self.backBtn.setIconSize(QSize(24, 24))
        self.backBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.backBtn.setAutoRaise(True)

        self.SideNav_Layout.addWidget(self.backBtn)


        self.CW_horizontalLayout.addWidget(self.sideNav, 0, Qt.AlignHCenter)

        self.content = QVBoxLayout()
        self.content.setSpacing(0)
        self.content.setObjectName(u"content")
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 70))
        self.topBar.setFrameShadow(QFrame.Raised)
        self.TopBarLayout = QHBoxLayout(self.topBar)
        self.TopBarLayout.setSpacing(0)
        self.TopBarLayout.setObjectName(u"TopBarLayout")
        self.TopBarLayout.setContentsMargins(0, 0, 0, 0)

        self.content.addWidget(self.topBar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.content.addWidget(self.stackedWidget)


        self.CW_horizontalLayout.addLayout(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.libraryBtn.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.sourcesBtn.setText(QCoreApplication.translate("MainWindow", u"Sources", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

