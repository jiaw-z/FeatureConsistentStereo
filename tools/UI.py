# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CostView(object):
    def setupUi(self, CostView):
        CostView.setObjectName("CostView")
        CostView.resize(1500, 741)
        self.widget = QtWidgets.QWidget(CostView)
        self.widget.setObjectName("widget")
        self.show_error_map = QtWidgets.QLabel(self.widget)
        self.show_error_map.setGeometry(QtCore.QRect(0, 0, 1500, 600))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.show_error_map.setFont(font)
        self.show_error_map.setTextFormat(QtCore.Qt.RichText)
        self.show_error_map.setAlignment(QtCore.Qt.AlignCenter)
        self.show_error_map.setObjectName("show_error_map")
        self.run = QtWidgets.QPushButton(self.widget)
        self.run.setGeometry(QtCore.QRect(210, 670, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.run.setFont(font)
        self.run.setIconSize(QtCore.QSize(20, 20))
        self.run.setObjectName("run")
        self.x = QtWidgets.QLabel(self.widget)
        self.x.setGeometry(QtCore.QRect(100, 660, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.x.setFont(font)
        self.x.setAlignment(QtCore.Qt.AlignCenter)
        self.x.setObjectName("x")
        self.y = QtWidgets.QLabel(self.widget)
        self.y.setGeometry(QtCore.QRect(100, 690, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.y.setFont(font)
        self.y.setAlignment(QtCore.Qt.AlignCenter)
        self.y.setObjectName("y")
        self.x_num = QtWidgets.QSpinBox(self.widget)
        self.x_num.setGeometry(QtCore.QRect(135, 660, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.x_num.setFont(font)
        self.x_num.setMaximum(1500)
        self.x_num.setObjectName("x_num")
        self.y_num = QtWidgets.QSpinBox(self.widget)
        self.y_num.setGeometry(QtCore.QRect(135, 690, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.y_num.setFont(font)
        self.y_num.setMaximum(600)
        self.y_num.setObjectName("y_num")
        self.showInfo = QtWidgets.QLabel(self.widget)
        self.showInfo.setGeometry(QtCore.QRect(290, 660, 880, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.showInfo.setFont(font)
        self.showInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.showInfo.setObjectName("showInfo")
        self.load_result = QtWidgets.QPushButton(self.widget)
        self.load_result.setGeometry(QtCore.QRect(100, 620, 190, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.load_result.setFont(font)
        self.load_result.setObjectName("load_result")
        CostView.setCentralWidget(self.widget)

        self.retranslateUi(CostView)
        self.load_result.clicked.connect(CostView.openDiag)
        self.run.clicked.connect(CostView.setXY_andRun)
        QtCore.QMetaObject.connectSlotsByName(CostView)

    def retranslateUi(self, CostView):
        _translate = QtCore.QCoreApplication.translate
        CostView.setWindowTitle(_translate("CostView", "MainWindow"))
        self.show_error_map.setText(_translate("CostView", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Disparity Error Map Display Window</span></p><p align=\"center\">Please press \'LoadResult\' button to load result. The result should be estimated by dmb/tools/demo.py.</p><p align=\"center\">Untill error map is loaded, click on error map to see the cost distribution on this point.</p></body></html>"))
        self.run.setText(_translate("CostView", "Run"))
        self.x.setText(_translate("CostView", "x:"))
        self.y.setText(_translate("CostView", "y:"))
        self.showInfo.setText(_translate("CostView", "It\'s a valid position: (0, 0)"))
        self.load_result.setText(_translate("CostView", "LoadResult"))
