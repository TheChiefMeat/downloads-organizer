# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from attributes import DOWNLOADS_DIRECTORY
from funcs import print_os_info, change_working_directory, list_all_files, sort_files_by_type, \
    move_files_to_folders
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import time
import sys

dl_dir = DOWNLOADS_DIRECTORY

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        change_working_directory(dl_dir)
        download_files = list_all_files(dl_dir)
        files_sorted = sort_files_by_type(download_files)
        move_files_to_folders(files_sorted)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 175)
        MainWindow.setMinimumSize(QtCore.QSize(358, 175))
        MainWindow.setMaximumSize(QtCore.QSize(358, 175))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(358, 175))
        self.centralwidget.setMaximumSize(QtCore.QSize(358, 175))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 312, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Start.setObjectName("Start")
        self.horizontalLayout.addWidget(self.Start)
        self.RunOnce = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RunOnce.setObjectName("RunOnce")
        self.horizontalLayout.addWidget(self.RunOnce)
        self.Stop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Stop.setObjectName("Stop")
        self.horizontalLayout.addWidget(self.Stop)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 231, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Start.clicked.connect(self.clicked)
        self.Stop.clicked.connect(self.stopped)
        self.RunOnce.clicked.connect(self.clickedOnce)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Organizer"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.RunOnce.setText(_translate("MainWindow", "Run Once"))
        self.Stop.setText(_translate("MainWindow", "Stop and Close"))
        self.label.setText(_translate("MainWindow", "Download Organzier"))

    def clicked(self):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, dl_dir, recursive=True)
        observer.start()

        print_os_info()
        print('Running Downloads Organizer...')
        self.label.setText("Download Organizer Running...")
        self.Start.setEnabled(False)
        self.RunOnce.setEnabled(False)

        #observer.join()

    def clickedOnce(self):
        MyHandler.on_modified(self, MainWindow)
        self.label.setText("Download Organizer Complete!")

    def stopped(self):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, dl_dir, recursive=True)
        observer.stop()
        self.label.setText("Download Organizer Closing...")

        app = QApplication(sys.argv)
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
