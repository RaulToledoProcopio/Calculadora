# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 500)
        MainWindow.setMinimumSize(QSize(725, 500))
        MainWindow.setMaximumSize(QSize(725, 500))
        font = QFont()
        font.setPointSize(1)
        font.setWeight(QFont.Thin)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow {\n"
"    background-color: #292b2c;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button1 = QPushButton(self.centralwidget)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(30, 370, 51, 31))
        font1 = QFont()
        self.button1.setFont(font1)
        self.button1.setStyleSheet(u"QPushButton#button1 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button1:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button2 = QPushButton(self.centralwidget)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(100, 370, 51, 31))
        self.button2.setStyleSheet(u"QPushButton#button2 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button2:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button2.setIconSize(QSize(16, 16))
        self.button3 = QPushButton(self.centralwidget)
        self.button3.setObjectName(u"button3")
        self.button3.setGeometry(QRect(170, 370, 51, 31))
        self.button3.setStyleSheet(u"QPushButton#button3 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button3:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button4 = QPushButton(self.centralwidget)
        self.button4.setObjectName(u"button4")
        self.button4.setGeometry(QRect(30, 310, 51, 31))
        self.button4.setStyleSheet(u"QPushButton#button4 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button4:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button5 = QPushButton(self.centralwidget)
        self.button5.setObjectName(u"button5")
        self.button5.setGeometry(QRect(100, 310, 51, 31))
        self.button5.setStyleSheet(u"QPushButton#button5 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button5:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button6 = QPushButton(self.centralwidget)
        self.button6.setObjectName(u"button6")
        self.button6.setGeometry(QRect(170, 310, 51, 31))
        self.button6.setStyleSheet(u"QPushButton#button6 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button6:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button0 = QPushButton(self.centralwidget)
        self.button0.setObjectName(u"button0")
        self.button0.setGeometry(QRect(30, 430, 51, 31))
        self.button0.setStyleSheet(u"QPushButton#button0 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button0:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonPunto = QPushButton(self.centralwidget)
        self.buttonPunto.setObjectName(u"buttonPunto")
        self.buttonPunto.setGeometry(QRect(100, 430, 51, 31))
        self.buttonPunto.setStyleSheet(u"QPushButton#buttonPunto {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonPunto:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonPorcentaje = QPushButton(self.centralwidget)
        self.buttonPorcentaje.setObjectName(u"buttonPorcentaje")
        self.buttonPorcentaje.setGeometry(QRect(170, 430, 51, 31))
        self.buttonPorcentaje.setStyleSheet(u"QPushButton#buttonPorcentaje {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonPorcentaje:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../Desktop/trollface_PNG2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonPorcentaje.setIcon(icon)
        self.buttonPorcentaje.setIconSize(QSize(32, 32))
        self.buttonSQR = QPushButton(self.centralwidget)
        self.buttonSQR.setObjectName(u"buttonSQR")
        self.buttonSQR.setGeometry(QRect(240, 430, 51, 31))
        self.buttonSQR.setStyleSheet(u"QPushButton#buttonSQR {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonSQR:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonIgual = QPushButton(self.centralwidget)
        self.buttonIgual.setObjectName(u"buttonIgual")
        self.buttonIgual.setGeometry(QRect(310, 430, 51, 31))
        self.buttonIgual.setStyleSheet(u"QPushButton#buttonIgual {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonIgual:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonMas = QPushButton(self.centralwidget)
        self.buttonMas.setObjectName(u"buttonMas")
        self.buttonMas.setGeometry(QRect(240, 370, 51, 31))
        self.buttonMas.setStyleSheet(u"QPushButton#buttonMas {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonMas:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonMenos = QPushButton(self.centralwidget)
        self.buttonMenos.setObjectName(u"buttonMenos")
        self.buttonMenos.setGeometry(QRect(310, 370, 51, 31))
        self.buttonMenos.setStyleSheet(u"QPushButton#buttonMenos {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonMenos:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonX = QPushButton(self.centralwidget)
        self.buttonX.setObjectName(u"buttonX")
        self.buttonX.setGeometry(QRect(240, 310, 51, 31))
        self.buttonX.setStyleSheet(u"QPushButton#buttonX {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonX:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonDividir = QPushButton(self.centralwidget)
        self.buttonDividir.setObjectName(u"buttonDividir")
        self.buttonDividir.setGeometry(QRect(310, 310, 51, 31))
        self.buttonDividir.setStyleSheet(u"QPushButton#buttonDividir {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonDividir:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button7 = QPushButton(self.centralwidget)
        self.button7.setObjectName(u"button7")
        self.button7.setGeometry(QRect(30, 250, 51, 31))
        self.button7.setStyleSheet(u"QPushButton#button7 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button7:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button8 = QPushButton(self.centralwidget)
        self.button8.setObjectName(u"button8")
        self.button8.setGeometry(QRect(100, 250, 51, 31))
        self.button8.setStyleSheet(u"QPushButton#button8 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button8:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.button9 = QPushButton(self.centralwidget)
        self.button9.setObjectName(u"button9")
        self.button9.setGeometry(QRect(170, 250, 51, 31))
        self.button9.setStyleSheet(u"QPushButton#button9 {\n"
"    background-color: #707070; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#button9:hover {\n"
"    background-color: #8A8A8A;\n"
"}\n"
"")
        self.buttonDel = QPushButton(self.centralwidget)
        self.buttonDel.setObjectName(u"buttonDel")
        self.buttonDel.setGeometry(QRect(240, 250, 51, 31))
        self.buttonDel.setStyleSheet(u"QPushButton#buttonDel {\n"
"    background-color: #894e5c; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonDel:hover {\n"
"    background-color: #a66d7d;\n"
"}\n"
"")
        self.buttonAC = QPushButton(self.centralwidget)
        self.buttonAC.setObjectName(u"buttonAC")
        self.buttonAC.setGeometry(QRect(310, 250, 51, 31))
        self.buttonAC.setStyleSheet(u"QPushButton#buttonAC {\n"
"    background-color: #894e5c; \n"
"    color: white;\n"
"    font-size: 15px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius:4px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonAC:hover {\n"
"    background-color: #a66d7d;\n"
"}\n"
"")
        self.Pantalla = QLabel(self.centralwidget)
        self.Pantalla.setObjectName(u"Pantalla")
        self.Pantalla.setGeometry(QRect(30, 50, 331, 51))
        font2 = QFont()
        font2.setFamilies([u"Seven Segment"])
        self.Pantalla.setFont(font2)
        self.Pantalla.setStyleSheet(u"QLabel#Pantalla {\n"
"    background-color: #91978d;\n"
"    color: black;\n"
"    font-size: 32px;\n"
"    font-family: \"Seven Segment\", \"Digital-7 Mono\", sans-serif;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}\n"
"")
        self.buttonSEN = QPushButton(self.centralwidget)
        self.buttonSEN.setObjectName(u"buttonSEN")
        self.buttonSEN.setGeometry(QRect(30, 200, 51, 20))
        self.buttonSEN.setStyleSheet(u"QPushButton#buttonSEN {\n"
"    background-color: #bfbfbf; \n"
"    color: white;\n"
"    font-size: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonSEN:hover {\n"
"    background-color: #d1d1d1;\n"
"}\n"
"")
        self.buttonCOS = QPushButton(self.centralwidget)
        self.buttonCOS.setObjectName(u"buttonCOS")
        self.buttonCOS.setGeometry(QRect(100, 200, 51, 21))
        self.buttonCOS.setStyleSheet(u"QPushButton#buttonCOS {\n"
"    background-color: #bfbfbf; \n"
"    color: white;\n"
"    font-size: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonCOS:hover {\n"
"    background-color: #d1d1d1;\n"
"}\n"
"")
        self.buttonON = QPushButton(self.centralwidget)
        self.buttonON.setObjectName(u"buttonON")
        self.buttonON.setGeometry(QRect(310, 200, 51, 21))
        self.buttonON.setStyleSheet(u"QPushButton#buttonON {\n"
"    background-color: #894e5c; \n"
"    color: white;\n"
"    font-size: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonON:hover {\n"
"    background-color: #a66d7d;\n"
"}\n"
"")
        self.buttonP1 = QPushButton(self.centralwidget)
        self.buttonP1.setObjectName(u"buttonP1")
        self.buttonP1.setGeometry(QRect(170, 200, 51, 21))
        self.buttonP1.setStyleSheet(u"QPushButton#buttonP1 {\n"
"    background-color: #bfbfbf; \n"
"    color: white;\n"
"    font-size: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonP1:hover {\n"
"    background-color: #d1d1d1;\n"
"}\n"
"")
        self.buttonP2 = QPushButton(self.centralwidget)
        self.buttonP2.setObjectName(u"buttonP2")
        self.buttonP2.setGeometry(QRect(240, 200, 51, 21))
        self.buttonP2.setStyleSheet(u"QPushButton#buttonP2 {\n"
"    background-color: #bfbfbf; \n"
"    color: white;\n"
"    font-size: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#buttonP2:hover {\n"
"    background-color: #d1d1d1;\n"
"}\n"
"")
        self.Logo = QLabel(self.centralwidget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(20, 0, 111, 51))
        self.Logo.setStyleSheet(u"QLabel#Logo {\n"
"    color: white;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"	font-weight: bold;\n"
"    qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        self.log = QTableWidget(self.centralwidget)
        if (self.log.columnCount() < 3):
            self.log.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.log.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.log.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.log.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(400, 50, 301, 411))
        self.log.setStyleSheet(u"QTableView#log {\n"
"    background-color: #91978d;\n"
"}")
        self.Modelo = QLabel(self.centralwidget)
        self.Modelo.setObjectName(u"Modelo")
        self.Modelo.setGeometry(QRect(170, 110, 201, 41))
        self.Modelo.setStyleSheet(u"QLabel#Modelo {\n"
"    color: #894e5c;\n"
"    font-size: 15px;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.buttonPunto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.buttonPorcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.buttonSQR.setText(QCoreApplication.translate("MainWindow", u"SQR", None))
        self.buttonIgual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.buttonMas.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.buttonMenos.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.buttonX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.buttonDividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.buttonDel.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.buttonAC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Pantalla.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.buttonSEN.setText(QCoreApplication.translate("MainWindow", u"SEN", None))
        self.buttonCOS.setText(QCoreApplication.translate("MainWindow", u"COS", None))
        self.buttonON.setText(QCoreApplication.translate("MainWindow", u"ON/OFF", None))
        self.buttonP1.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.buttonP2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        ___qtablewidgetitem = self.log.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Operacion", None));
        ___qtablewidgetitem1 = self.log.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem2 = self.log.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        self.Modelo.setText(QCoreApplication.translate("MainWindow", u"Calculator Blaster 3000", None))
    # retranslateUi

