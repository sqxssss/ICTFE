from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem
from PyQt5.QtWidgets import QFileDialog

from ui_Widgets import uni_Widget
from ui_Widgets.ErrorWin import errorInfo
from PyQt5 import Qt, QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import os


class ui_TerminalPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_TerminalPanel, self).__init__()

        self.CyberChefPanel = CyberChefPanelWidget(self)
        self.CyberChefPanel.setObjectName('CyberChefPanel')
        self.CyberChefPanel.setStyleSheet('background-color: transparent;')
        self.CyberChefPanel.setGeometry(0, 0, 1428, 768)


class CyberChefPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CyberChefPanelWidget, self).__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        print('file:///' + pwd + '/CyberChef/CyberChef.html')
        self.browser.load(QtCore.QUrl('file:///' + pwd + '/CyberChef/CyberChef.html'))
        self.browser.setGeometry(QtCore.QRect(0, 0, 1428, 768))
        self.browser.show()
        self.browser.page().profile().downloadRequested.connect(self.on_downloadRequested)

    def on_downloadRequested(self, download: "QWebEngineDownloadItem"):
        # download是QWebEngineDownloadItem对象；
        # 下载文件的保存路径及文件名
        old_path = download.path()
        suffix = QFileInfo(old_path).suffix()
        # 下载文件类型
        filttype = download.mimeType()
        # 后缀切割
        unkonw_suffix = filttype.split(r'/')[-1]
        path, _ = QFileDialog.getSaveFileName(self, "保存到", old_path, "*." + unkonw_suffix + ";;" + "*." + suffix)
        print(old_path, suffix)
        if path != "":
            download.setPath(path)
            download.accept()