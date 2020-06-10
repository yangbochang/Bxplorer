# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\GitHub\Bxplorer\src\bxplorer_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 633)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 0, 1, 1)
        self.tableView_file = QtWidgets.QTableView(self.centralwidget)
        self.tableView_file.setObjectName("tableView_file")
        self.gridLayout.addWidget(self.tableView_file, 1, 0, 1, 1)
        self.tableView_filter = QtWidgets.QTableView(self.centralwidget)
        self.tableView_filter.setObjectName("tableView_filter")
        self.gridLayout.addWidget(self.tableView_filter, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.label_root = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_root.setFont(font)
        self.label_root.setObjectName("label_root")
        self.gridLayout.addWidget(self.label_root, 4, 0, 1, 1)
        self.tableView_root = QtWidgets.QTableView(self.centralwidget)
        self.tableView_root.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_root.setObjectName("tableView_root")
        self.gridLayout.addWidget(self.tableView_root, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.tableView_suffix = QtWidgets.QTableView(self.centralwidget)
        self.tableView_suffix.setShowGrid(False)
        self.tableView_suffix.setObjectName("tableView_suffix")
        self.gridLayout.addWidget(self.tableView_suffix, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableView_file, self.tableView_filter)
        MainWindow.setTabOrder(self.tableView_filter, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.tableView_suffix)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_file.setText(_translate("MainWindow", "文件"))
        self.label_root.setText(_translate("MainWindow", "文件夹"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
