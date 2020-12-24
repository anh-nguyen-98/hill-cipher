from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import QMainWindow, QWidget, QStackedWidget, QScrollArea, QFrame, QVBoxLayout, QSizePolicy, QLabel, \
    QPushButton, QHBoxLayout, QGroupBox, QRadioButton, QLineEdit



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cryptography')
        self.setFixedSize(1218, 800)
        self.setWindowIcon(QIcon("../images/app_icon.jpeg"))
        self.centralwidget = QWidget(self)
        self.create_centralwidget_display()
        self.setCentralWidget(self.centralwidget)

        self.ecp_continue_btn.setVisible(False)
        self.dcp_continue_btn.setVisible(False)

    def create_home_pg(self):
        self.home_pg = QtWidgets.QWidget()
        self.home_pg.setObjectName("home_pg")
        self.scrollArea = QtWidgets.QScrollArea(self.home_pg)
        self.scrollArea.setGeometry(QtCore.QRect(-10, -50, 1281, 831))
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1312, 1531))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(1290, 751))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel("CRYPTOGRAPHY", self.widget)
        self.label_4.setGeometry(QtCore.QRect(270, 210, 761, 151))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(55)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(65, 58, 218);\n"
                                   "font: 75 55pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 1251, 731))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/homepg/homepg_bg.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel("TEAM ENIGMA", self.widget)
        self.label_6.setGeometry(QtCore.QRect(520, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(183, 92, 74);\n"
                                   "font: 20pt \"MS Shell Dlg 2\";\n"
                                   "font-weight: bold\n"
                                   "")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel("​Nguyen Hoang Nam Anh - Nguyen Bao Ngoc \nLinear Algebra / Fall 2020\n\nInstructor: Dr. Linh Tran\n\n​Fulbright University Vietnam", self.widget)
        self.label_7.setGeometry(QtCore.QRect(430, 420, 441, 201))
        self.label_7.setStyleSheet("color: rgb(65, 58, 218);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(530, 70, 211, 161))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../images/homepg/homepg_earth.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(860, 550, 101, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../images/homepg/homepg_hammer.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(400, 600, 90, 90))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../images/homepg/homepg_cal.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 751))
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1291, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setStyleSheet("background-color:rgb(65, 58, 218)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel("​Provide for\nsecure communication \non social networks ", self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(330, 170, 631, 201))
        self.label_11.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 28pt \"MS Shell Dlg 2\";\n"
                                    "background-color:rgb(65, 58, 218)")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel("​In the digital era, people’s communication is easily exposed and secretly read by outsiders of the conversation.\n"
"\n"
"Cryptography is applied in our products to help senders encode their message [ENCIPHER] and help receivers decode the corresponding message [DECIPHER].",self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(370, 380, 561, 181))
        self.label_12.setStyleSheet("background-color:rgb(65, 58, 218);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(600, 80, 91, 71))
        self.label_13.setStyleSheet("background-color:rgb(65, 58, 218)")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("../images/homepg/homepg_laptop.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.learnmore = QtWidgets.QPushButton("Learn More", self.widget_2)
        self.learnmore.setGeometry(QtCore.QRect(570, 600, 161, 51))
        self.learnmore.setStyleSheet("background-color:rgb(65, 58, 218);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "border: 1px solid rgb(255, 255, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font-weight: 500")
        self.learnmore.setObjectName("learnmore")
        self.label_5.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.learnmore.raise_()
        self.label_11.raise_()
        self.verticalLayout_2.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.home_pg)


    def create_about_us_pg(self):
        self.about_us_pg = QWidget()
        self.scrollArea_2 = QScrollArea(self.about_us_pg)
        self.scrollArea_2.setGeometry(0, -20, 1281, 771)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(0, 0, 98, 1543)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.widget_4 = QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 375))

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setGeometry(10, 0, 1251, 391)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(0, 50))
        self.label_27.setStyleSheet("background-color: rgb(248, 200, 83)")


        self.label_28 = QLabel("About Us", self.widget_4)
        self.label_28.setGeometry(260, 80, 791, 91)
        self.label_28.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 75 30pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)

        self.label_29 = QLabel("<html><head/><body><p>Cryptography is applied in our products to help senders encode their message <span style=\" font-weight:600;\">[ENCIPHER] </span>and help receivers decode the corresponding message<span style=\" font-weight:600;\"> [DECIPHER].</span></p></body></html>", self.widget_4)
        self.label_29.setGeometry(260, 150, 781, 171)
        self.label_29.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setWordWrap(True)
        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 375))

        self.label_18 = QLabel(self.widget_5)
        self.label_18.setGeometry(-50, -10, 671, 391)
        self.label_18.setText("")
        self.label_18.setPixmap(QPixmap("../images/aboutuspg/laptop.jpg"))
        self.label_18.setScaledContents(True)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setGeometry(610, 0, 621, 381)

        self.label_19 = QLabel(self.widget_7)
        self.label_19.setGeometry(10, -10, 621, 401)
        self.label_19.setStyleSheet("background-color:rgb(255, 255, 255)")


        self.label_20 = QLabel("​About Cryptography​", self.widget_7)
        self.label_20.setGeometry(10, 50, 611, 111)
        self.label_20.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)

        self.label_21 = QLabel("<html><head/><body><p><span style=\" font-size:9pt;\">​In the language of cryptography, codes are called ciphers, uncoded messages are called </span><span style=\" font-size:9pt; font-weight:600;\">plaintext</span><span style=\" font-size:9pt;\">, and coded messages are called </span><span style=\" font-size:9pt; font-weight:600;\">cipher-text</span><span style=\" font-size:9pt;\">. ​</span></p><p><span style=\" font-size:9pt;\">The process of converting from plaintext to cipher-text is called </span><span style=\" font-size:9pt; font-weight:600;\">enciphering</span><span style=\" font-size:9pt;\">, and the reverse process of converting from cipher-text to plaintext is called </span><span style=\" font-size:9pt; font-weight:600;\">deciphering</span><span style=\" font-size:9pt;\">. ​</span></p></body></html>", self.widget_7)
        self.label_21.setGeometry(120, 130, 411, 201)
        self.label_21.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setWordWrap(True)

        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 375))

        self.label_22 = QLabel(self.widget_6)
        self.label_22.setGeometry(310, 4, 671, 381)
        self.label_22.setStyleSheet("background-color:rgb(65, 58, 218)")
        self.label_22.setText("")

        self.label_23 = QLabel("​​Linear Algebra Application", self.widget_6)
        self.label_23.setGeometry(320, 40, 661, 91)
        self.label_23.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "\n"
                                    "font: 25pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)

        self.label_25 = QLabel(self.widget_6)
        self.label_25.setGeometry(980, 4, 261, 371)
        self.label_25.setFrameShadow(QFrame.Sunken)
        self.label_25.setText("")
        self.label_25.setPixmap(QPixmap("../images/aboutuspg/bg.png"))
        self.label_25.setScaledContents(True)

        self.label_26 = QLabel(self.widget_6)
        self.label_26.setGeometry(-6, 4, 321, 381)
        self.label_26.setText("")
        self.label_26.setPixmap(QPixmap("../images/aboutuspg/bg.png"))
        self.label_26.setScaledContents(True)

        self.label_24 = QLabel("<html><head/><body><p><span style=\" font-size:10pt;\">​We can encipher the plaintext that replaces each letter of the alphabet with a different letter (called substitution ciphers) - the simplest enciphering way but too easy to break. ​</span><br/></p><p><span style=\" font-size:10pt;\">Therefore, we divide the plaintext into groups of letters and encipher the plaintext group by group, rather than one letter at a time - the polygraphic system based on matrix transformations.</span></p></body></html>", self.widget_6)
        self.label_24.setGeometry(400, 140, 500, 191)
        self.label_24.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setWordWrap(True)

        self.verticalLayout.addWidget(self.widget_6)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 375))

        self.horizontalLayoutWidget_2 = QWidget(self.widget_3)
        self.horizontalLayoutWidget_2.setGeometry(280, 180, 671, 102)

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.ecp_btn_aboutus = QPushButton("Encipher >", self.horizontalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecp_btn_aboutus.sizePolicy().hasHeightForWidth())
        self.ecp_btn_aboutus.setSizePolicy(sizePolicy)
        self.ecp_btn_aboutus.setMinimumSize(QtCore.QSize(200, 50))
        self.ecp_btn_aboutus.setStyleSheet("color:rgb(65, 58, 218);\n"
                                           "background-color: rgb(255,255,255);\n"
                                           "border: 0.5px solid rgb(65, 58, 218);")

        self.horizontalLayout.addWidget(self.ecp_btn_aboutus)
        self.dcp_btn_aboutus = QPushButton("Decipher >", self.horizontalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dcp_btn_aboutus.sizePolicy().hasHeightForWidth())
        self.dcp_btn_aboutus.setSizePolicy(sizePolicy)
        self.dcp_btn_aboutus.setMinimumSize(QtCore.QSize(200, 50))
        self.dcp_btn_aboutus.setStyleSheet("color:rgb(65, 58, 218);\n"
                                           "background-color: rgb(255,255,255);\n"
                                           "border: 0.5px solid rgb(65, 58, 218);")

        self.horizontalLayout.addWidget(self.dcp_btn_aboutus)
        self.label_31 = QLabel(self.widget_3)
        self.label_31.setGeometry(0, -10, 1241, 391)
        self.label_31.setStyleSheet("background-color: rgb(248, 200, 83)")


        self.label_30 = QLabel("Join Us Now", self.widget_3)
        self.label_30.setGeometry(20, 40, 1211, 71)
        self.label_30.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 25pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)

        self.label_47 = QLabel(self.widget_3)
        self.label_47.setGeometry(550, 110, 141, 71)
        self.label_47.setText("")
        self.label_47.setPixmap(QPixmap("../images/aboutuspg/girls_icon.png"))
        self.label_47.setScaledContents(True)

        self.label_31.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_30.raise_()
        self.label_47.raise_()
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.about_us_pg)

    def create_encipher_page(self):
        self.ecp_pg = QWidget()
        self.ecp_pg.setStyleSheet("color: rgb(248, 200, 83)")

        self.label_2 = QLabel(self.ecp_pg)
        self.label_2.setGeometry(-10, 0, 1261, 741)
        self.label_2.setStyleSheet("background-color:rgb(65, 58, 218)")


        self.verticalLayoutWidget_4 = QWidget(self.ecp_pg)
        self.verticalLayoutWidget_4.setGeometry(190, 50, 881, 661)

        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel("Encipher", self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(0, 70))
        self.label_16.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_16)
        self.label_17 = QLabel("​Deliver your message in secret", self.verticalLayoutWidget_4)
        self.label_17.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_17)
        self.label_50 = QLabel(self.verticalLayoutWidget_4)
        self.label_50.setText("")
        self.label_50.setPixmap(QPixmap("../images/ecppg/line.png"))
        self.label_50.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_50)
        self.groupBox_2 = QGroupBox("Your type of alphabet is ...", self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 125))

        self.groupBox_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                      "font-weight:bold;")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_7.setGeometry(0, 10, 881, 111)

        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.ecp_type_alpha26 = QRadioButton("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.verticalLayoutWidget_7)
        self.ecp_type_alpha26.setStyleSheet("font-weight: normal")

        self.verticalLayout_10.addWidget(self.ecp_type_alpha26)
        self.ecp_type_alpha36 = QRadioButton("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", self.verticalLayoutWidget_7)
        self.ecp_type_alpha36.setStyleSheet("font-weight: normal")

        self.verticalLayout_10.addWidget(self.ecp_type_alpha36)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox = QGroupBox("Your type of password is ...", self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 125))
        self.groupBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold;\n"
                                    "")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setGeometry(0, 10, 879, 111)

        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.ecp_pw_num_type = QRadioButton("​Number (123 ... )", self.verticalLayoutWidget_6)
        self.ecp_pw_num_type.setStyleSheet("font-weight: normal")

        self.verticalLayout_9.addWidget(self.ecp_pw_num_type)
        self.ecp_pw_alpha_type = QRadioButton("Alphabet (AaBbCc ... )", self.verticalLayoutWidget_6)
        self.ecp_pw_alpha_type.setStyleSheet("font-weight: normal")

        self.verticalLayout_9.addWidget(self.ecp_pw_alpha_type)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_3 = QVBoxLayout()

        self.label_33 = QLabel("<html><head/><body><p><span style=\" font-weight:600;\">Enter your password</span></p><p>Password has to include (4, 16, 25, 36, 49, ..., n^2) letters.</p></body></html>",self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QtCore.QSize(0, 50))
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 50))


        self.label_33.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_33)
        self.ecp_pw_lineEdit = QLineEdit(self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecp_pw_lineEdit.sizePolicy().hasHeightForWidth())
        self.ecp_pw_lineEdit.setSizePolicy(sizePolicy)
        self.ecp_pw_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.ecp_pw_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ecp_pw_lineEdit.setStyleSheet("color: rgb(0, 0, 0)")
        self.ecp_pw_lineEdit.setText("")
        self.ecp_pw_lineEdit.setEchoMode(QLineEdit.Password)
        self.ecp_pw_lineEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.ecp_pw_lineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.ecp_done_btn = QPushButton("OK", self.verticalLayoutWidget_4)


        self.ecp_done_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font-weight: bold")

        self.verticalLayout_6.addWidget(self.ecp_done_btn)
        self.ecp_pw_status = QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecp_pw_status.sizePolicy().hasHeightForWidth())
        self.ecp_pw_status.setSizePolicy(sizePolicy)
        self.ecp_pw_status.setMinimumSize(QtCore.QSize(0, 70))
        self.ecp_pw_status.setMaximumSize(QtCore.QSize(16777215, 70))
        self.ecp_pw_status.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font-weight: bold")
        self.ecp_pw_status.setText("")
        self.ecp_pw_status.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.ecp_pw_status)
        self.ecp_continue_btn = QPushButton("Continue", self.verticalLayoutWidget_4)


        self.ecp_continue_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font-weight: bold")

        self.verticalLayout_6.addWidget(self.ecp_continue_btn)
        self.label_48 = QLabel(self.ecp_pg)
        self.label_48.setGeometry(730, 60, 71, 61)
        self.label_48.setText("")
        self.label_48.setPixmap(QPixmap("../images/ecppg/mailbox.png"))
        self.label_48.setScaledContents(True)

        self.label_49 = QLabel(self.ecp_pg)
        self.label_49.setGeometry(786, 131, 41, 41)
        self.label_49.setText("")
        self.label_49.setPixmap(QPixmap("../images/ecppg/message.png"))
        self.label_49.setScaledContents(True)

        self.stackedWidget.addWidget(self.ecp_pg)


    def create_decipher_page(self):
        self.dcp_pg = QWidget()
        self.dcp_pg.setStyleSheet("color: rgb(248, 200, 83)")

        self.label_36 = QLabel(self.dcp_pg)
        self.label_36.setGeometry(-10, 0, 1261, 741)
        self.label_36.setStyleSheet("background-color:rgb(65, 58, 218)")
        self.label_36.setText("")

        self.verticalLayoutWidget_5 = QWidget(self.dcp_pg)
        self.verticalLayoutWidget_5.setGeometry(190, 50, 881, 660)

        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.label_37 = QLabel("Decipher", self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QtCore.QSize(0, 70))
        self.label_37.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold;\n"
                                    "color: rgb(248, 200, 83)")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_37)
        self.label_38 = QLabel("​Uncover your secret message", self.verticalLayoutWidget_5)
        self.label_38.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_38)
        self.label_51 = QLabel(self.verticalLayoutWidget_5)
        self.label_51.setText("")
        self.label_51.setPixmap(QPixmap("../images/ecppg/line.png"))
        self.label_51.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_51)
        self.groupBox_3 = QGroupBox("Your type of alphabet is ...", self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 125))
        self.groupBox_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                      "font-weight:bold;\n"
                                      "")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayoutWidget_8 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_8.setGeometry(0, 10, 881, 126)

        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_8)

        self.dcp_type_alpha26 = QRadioButton("ABCDEFGHIJKLMNOPQRSTUVWXYZ", self.verticalLayoutWidget_8)
        self.dcp_type_alpha26.setStyleSheet("font-weight: normal")

        self.verticalLayout_11.addWidget(self.dcp_type_alpha26)
        self.dcp_type_alpha36 = QRadioButton("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", self.verticalLayoutWidget_8)
        self.dcp_type_alpha36.setStyleSheet("font-weight: normal")

        self.verticalLayout_11.addWidget(self.dcp_type_alpha36)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QGroupBox("Your type of password is ...", self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 125))
        self.groupBox_4.setStyleSheet("\n"
                                      "font: 8pt \"MS Shell Dlg 2\";\n"
                                      "font-weight:bold;\n"
                                      "")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayoutWidget_9 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_9.setGeometry(0, 10, 879, 111)

        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.dcp_pw_num_type = QRadioButton("​Number (123 ... )", self.verticalLayoutWidget_9)
        self.dcp_pw_num_type.setStyleSheet("font-weight: normal")

        self.verticalLayout_12.addWidget(self.dcp_pw_num_type)
        self.dcp_pw_alpha_type = QRadioButton("Alphabet (AaBbCc ... )", self.verticalLayoutWidget_9)
        self.dcp_pw_alpha_type.setStyleSheet("font-weight: normal")

        self.verticalLayout_12.addWidget(self.dcp_pw_alpha_type)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.verticalLayout_4 = QVBoxLayout()

        self.label_40 = QLabel("<html><head/><body><p><span style=\" font-weight:600;\">Enter your password</span></p><p>Password has to include (4, 16, 25, 36, 49, ..., n^2) letters.</p></body></html>", self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QtCore.QSize(0, 50))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_40.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_40)
        self.dcp_pw_lineEdit = QLineEdit(self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dcp_pw_lineEdit.sizePolicy().hasHeightForWidth())
        self.dcp_pw_lineEdit.setSizePolicy(sizePolicy)
        self.dcp_pw_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dcp_pw_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dcp_pw_lineEdit.setStyleSheet("color: rgb(0, 0, 0)")
        self.dcp_pw_lineEdit.setText("")
        self.dcp_pw_lineEdit.setEchoMode(QLineEdit.Password)
        self.dcp_pw_lineEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.dcp_pw_lineEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.dcp_done_btn = QPushButton("OK", self.verticalLayoutWidget_5)
        self.dcp_done_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                        "font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font-weight: bold")

        self.verticalLayout_7.addWidget(self.dcp_done_btn)
        self.dcp_pw_status = QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dcp_pw_status.sizePolicy().hasHeightForWidth())
        self.dcp_pw_status.setSizePolicy(sizePolicy)
        self.dcp_pw_status.setMinimumSize(QtCore.QSize(0, 70))
        self.dcp_pw_status.setMaximumSize(QtCore.QSize(16777215, 70))
        self.dcp_pw_status.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
                                         "font-weight: bold")
        self.dcp_pw_status.setText("")
        self.dcp_pw_status.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.dcp_pw_status)
        self.dcp_continue_btn = QPushButton("Continue", self.verticalLayoutWidget_5)


        self.dcp_continue_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font-weight: bold")

        self.verticalLayout_7.addWidget(self.dcp_continue_btn)
        self.label_52 = QLabel(self.dcp_pg)
        self.label_52.setGeometry(730, 60, 71, 61)
        self.label_52.setText("")
        self.label_52.setPixmap(QPixmap("../images/ecppg/mailbox.png"))
        self.label_52.setScaledContents(True)

        self.label_53 = QLabel(self.dcp_pg)
        self.label_53.setGeometry(780, 130, 41, 41)
        self.label_53.setText("")
        self.label_53.setPixmap(QPixmap("../images/ecppg/message.png"))
        self.label_53.setScaledContents(True)

        self.stackedWidget.addWidget(self.dcp_pg)

    def create_team_pg(self):
        self.team_pg = QWidget()
        self.verticalLayoutWidget_3 = QWidget(self.team_pg)
        self.verticalLayoutWidget_3.setGeometry(0, 0, 1251, 769)

        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.widget_9 = QWidget(self.verticalLayoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 375))
        self.widget_9.setStyleSheet("background-color:rgb(65, 58, 218);\n"
                                    "color:rgb(255, 255, 255)")

        self.label_32 = QLabel("​Our Sharing", self.widget_9)
        self.label_32.setGeometry(40, 0, 1221, 101)
        self.label_32.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)

        self.label_44 = QLabel("<html><head/><body><p>​We are undergraduates from <span style=\" font-weight:600;\">Fulbright University Vietnam</span> that have pursued the interest of cryptography. Within the scale of Linear Algebra class, we are creating a cryptography product that helps clients encode their message and deliver it in secret and vice versa. Their receivers are able to decode those message from them.</p><p>Even though this is a class-scale project, it hopefully ensures the security of communication on social network by Linear Algebra application.  </p></body></html>", self.widget_9)
        self.label_44.setGeometry(350, 100, 591, 221)
        self.label_44.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.widget_9)
        self.widget_8 = QWidget(self.verticalLayoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 375))

        self.label_34 = QLabel(self.widget_8)
        self.label_34.setGeometry(40, 20, 281, 291)
        self.label_34.setText("")
        self.label_34.setPixmap(QPixmap("../images/teampg/christine.jpg"))
        self.label_34.setScaledContents(True)

        self.label_35 = QLabel("​Nam Anh ", self.widget_8)
        self.label_35.setGeometry(346, 90, 281, 61)
        self.label_35.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 22pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)

        self.label_39 = QLabel(self.widget_8)
        self.label_39.setGeometry(620, 20, 381, 301)
        self.label_39.setText("")
        self.label_39.setPixmap(QPixmap("../images/teampg/bijou.jpeg"))
        self.label_39.setScaledContents(True)

        self.label_43 = QLabel("Bao Ngoc", self.widget_8)
        self.label_43.setGeometry(976, 90, 271, 61)
        self.label_43.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 22pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)

        self.label_45 = QLabel("​Undergraduate U19", self.widget_8)
        self.label_45.setGeometry(350, 140, 271, 71)
        self.label_45.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";\n"
                                    "")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46 = QLabel("​Undergraduate U19", self.widget_8)
        self.label_46.setGeometry(980, 140, 271, 71)
        self.label_46.setStyleSheet("color:rgb(65, 58, 218);\n"
                                    "font: 12pt \"MS Shell Dlg 2\";\n"
                                    "")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.widget_8)
        self.stackedWidget.addWidget(self.team_pg)


    def create_encipher_pg_2(self):
        self.ecp_pg_2 = QWidget()

        self.label_58 = QLabel(self.ecp_pg_2)
        self.label_58.setGeometry(30, 0, 1221, 751)
        self.label_58.setStyleSheet("background-color:rgb(65, 58, 218)")
        self.label_58.setText("")

        self.verticalLayoutWidget_11 = QWidget(self.ecp_pg_2)
        self.verticalLayoutWidget_11.setGeometry(190, 60, 881, 621)

        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.label_59 = QLabel("Encipher", self.verticalLayoutWidget_11)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        self.label_59.setMinimumSize(QtCore.QSize(0, 70))
        self.label_59.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold;\n"
                                    "color: rgb(248, 200, 83)")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_59)
        self.label_60 = QLabel("​Deliver your message in secret", self.verticalLayoutWidget_11)
        self.label_60.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(248, 200, 83)")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_60)
        self.label_61 = QLabel(self.verticalLayoutWidget_11)
        self.label_61.setText("")
        self.label_61.setPixmap(QPixmap("../images/ecppg/line.png"))
        self.label_61.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_61)
        self.ecp_msg_label = QLabel("Enter your plaintext", self.verticalLayoutWidget_11)
        self.ecp_msg_label.setStyleSheet("color: rgb(248, 200, 83);\n"
                                         "font: 9pt \"MS Shell Dlg 2\";\n"
                                         "font-weight: bold;")
        self.ecp_msg_label.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.ecp_msg_label)
        self.ecp_msg_lineEdit = QLineEdit(self.verticalLayoutWidget_11)
        self.ecp_msg_lineEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.ecp_msg_lineEdit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.ecp_msg_lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.ecp_msg_lineEdit)
        self.verticalLayout_15 = QVBoxLayout()

        self.ecp_encode_btn = QPushButton("Encipher", self.verticalLayoutWidget_11)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecp_encode_btn.sizePolicy().hasHeightForWidth())
        self.ecp_encode_btn.setSizePolicy(sizePolicy)
        self.ecp_encode_btn.setMaximumSize(QtCore.QSize(1269, 16777215))
        self.ecp_encode_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ecp_encode_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                          "font: 9pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font-weight: bold")

        self.verticalLayout_15.addWidget(self.ecp_encode_btn)
        self.ecp_ret_label = QLabel(self.verticalLayoutWidget_11)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecp_ret_label.sizePolicy().hasHeightForWidth())
        self.ecp_ret_label.setSizePolicy(sizePolicy)
        self.ecp_ret_label.setMinimumSize(QtCore.QSize(0, 150))
        self.ecp_ret_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 9pt \"MS Shell Dlg 2\";\n"
                                         "font-weight:bold")
        self.ecp_ret_label.setText("")
        self.ecp_ret_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.verticalLayout_15.addWidget(self.ecp_ret_label)
        self.verticalLayout_13.addLayout(self.verticalLayout_15)
        self.label_63 = QLabel(self.ecp_pg_2)
        self.label_63.setGeometry(730, 70, 71, 61)
        self.label_63.setText("")
        self.label_63.setPixmap(QPixmap("../images/ecppg/mailbox.png"))
        self.label_63.setScaledContents(True)

        self.label_64 = QLabel(self.ecp_pg_2)
        self.label_64.setGeometry(780, 140, 41, 41)
        self.label_64.setText("")
        self.label_64.setPixmap(QPixmap("../images/ecppg/message.png"))
        self.label_64.setScaledContents(True)

        self.stackedWidget.addWidget(self.ecp_pg_2)

    def create_decipher_pg_2(self):
        self.dcp_pg_2 = QWidget()

        self.verticalLayoutWidget_10 = QWidget(self.dcp_pg_2)
        self.verticalLayoutWidget_10.setGeometry(190, 60, 881, 621)

        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.label_41 = QLabel("Decipher", self.verticalLayoutWidget_10)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QtCore.QSize(0, 70))
        self.label_41.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
                                    "font-weight:bold;\n"
                                    "color: rgb(248, 200, 83)")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_41)
        self.label_42 = QLabel("Uncover your secret message", self.verticalLayoutWidget_10)
        self.label_42.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(248, 200, 83)")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_42)
        self.label_54 = QLabel(self.verticalLayoutWidget_10)
        self.label_54.setText("")
        self.label_54.setPixmap(QPixmap("../images/ecppg/line.png"))
        self.label_54.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_54)
        self.dcp_msg_label = QLabel("Enter your ciphertext", self.verticalLayoutWidget_10)
        self.dcp_msg_label.setStyleSheet("color: rgb(248, 200, 83);\n"
                                         "font: 9pt \"MS Shell Dlg 2\";\n"
                                         "font-weight: bold;")
        self.dcp_msg_label.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.dcp_msg_label)
        self.dcp_msg_lineEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.dcp_msg_lineEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.dcp_msg_lineEdit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.dcp_msg_lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.dcp_msg_lineEdit)
        self.dcp_encode_btn = QPushButton("Decipher", self.verticalLayoutWidget_10)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dcp_encode_btn.sizePolicy().hasHeightForWidth())
        self.dcp_encode_btn.setSizePolicy(sizePolicy)
        self.dcp_encode_btn.setMaximumSize(QtCore.QSize(1269, 16777215))
        self.dcp_encode_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dcp_encode_btn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                          "font: 9pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font-weight: bold")

        self.verticalLayout_8.addWidget(self.dcp_encode_btn)
        self.dcp_ret_label = QLabel(self.verticalLayoutWidget_10)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dcp_ret_label.sizePolicy().hasHeightForWidth())
        self.dcp_ret_label.setSizePolicy(sizePolicy)
        self.dcp_ret_label.setMinimumSize(QtCore.QSize(0, 150))
        self.dcp_ret_label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                         "font: 9pt \"MS Shell Dlg 2\";\n"
                                         "font-weight: bold")
        self.dcp_ret_label.setText("")
        self.dcp_ret_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.dcp_ret_label)
        self.label_56 = QLabel(self.dcp_pg_2)
        self.label_56.setGeometry(30, 0, 1221, 731)
        self.label_56.setStyleSheet("background-color:rgb(65, 58, 218);\n"
                                    "color:rgb(255, 255, 255)")
        self.label_56.setText("")

        self.label_55 = QLabel(self.dcp_pg_2)
        self.label_55.setGeometry(730, 70, 71, 61)
        self.label_55.setText("")
        self.label_55.setPixmap(QPixmap("../images/ecppg/mailbox.png"))
        self.label_55.setScaledContents(True)

        self.label_57 = QLabel(self.dcp_pg_2)
        self.label_57.setGeometry(790, 150, 41, 41)
        self.label_57.setText("")
        self.label_57.setPixmap(QPixmap("../images/ecppg/message.png"))
        self.label_57.setScaledContents(True)

        self.label_56.raise_()
        self.verticalLayoutWidget_10.raise_()
        self.label_55.raise_()
        self.label_57.raise_()
        self.stackedWidget.addWidget(self.dcp_pg_2)

    def create_stacked_widget(self):
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QRect(-30, 70, 1251, 751))

        self.create_home_pg()
        self.create_about_us_pg()
        self.create_encipher_page()
        self.create_encipher_pg_2()
        self.create_decipher_page()
        self.create_decipher_pg_2()
        self.create_team_pg()

    def create_buttons(self):
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(330, 30, 618, 41)

        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.homebtn = QPushButton("Home", self.horizontalLayoutWidget)

        self.homebtn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                   "color: rgb(65, 58, 218);\n"
                                   "")

        self.horizontalLayout_2.addWidget(self.homebtn)
        self.aboutusbtn = QPushButton("About us", self.horizontalLayoutWidget)

        self.aboutusbtn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                      "color: rgb(65, 58, 218);\n"
                                      "")

        self.horizontalLayout_2.addWidget(self.aboutusbtn)
        self.encipherbtn = QPushButton("Encipher", self.horizontalLayoutWidget)

        self.encipherbtn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                       "color: rgb(65, 58, 218);\n"
                                       "\n"
                                       "")

        self.horizontalLayout_2.addWidget(self.encipherbtn)
        self.decipherbtn = QPushButton("Decipher", self.horizontalLayoutWidget)

        self.decipherbtn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                       "color: rgb(65, 58, 218);\n"
                                       "")

        self.horizontalLayout_2.addWidget(self.decipherbtn)
        self.teambtn = QPushButton("Team", self.horizontalLayoutWidget)

        self.teambtn.setStyleSheet("background-color: rgb(248, 200, 83);\n"
                                   "color: rgb(65, 58, 218);")

        self.horizontalLayout_2.addWidget(self.teambtn)


    def create_centralwidget_display(self):
        self.create_buttons()
        self.create_stacked_widget()

        self.label_15 = QLabel(self.centralwidget)

        self.label_15.setGeometry(-20, 30, 1241, 41)
        self.label_15.setStyleSheet("background-color: rgb(248, 200, 83)")
        self.label_15.setText("")
        self.label = QLabel("                 ​Project Cryptography is for people\'s secure communication and for our grade A!!!", self.centralwidget)
        self.label.setGeometry(1, -9, 1221, 41)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))

        self.label.setStyleSheet("background-color:rgb(65, 58, 218);\n"
                                 "color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_14 = QLabel( "Project \nCryptography", self.centralwidget)
        self.label_14.setGeometry(20, 40, 261, 81)

        self.label_14.setStyleSheet("color:rgb(255, 255, 255);\n"
                                    "font: 14pt \"MS Shell Dlg 2\";\n"
                                    "font-weight: bold")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)



        self.label_15.raise_()
        self.label.raise_()
        self.stackedWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_14.raise_()



