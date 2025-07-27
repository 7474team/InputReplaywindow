# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QListView, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(877, 453)
        self.horizontalLayout_11 = QHBoxLayout(Dialog)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.MOUXY_label = QLabel(Dialog)
        self.MOUXY_label.setObjectName(u"MOUXY_label")

        self.horizontalLayout_7.addWidget(self.MOUXY_label)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.speed_lebel_3 = QLabel(Dialog)
        self.speed_lebel_3.setObjectName(u"speed_lebel_3")
        self.speed_lebel_3.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_9.addWidget(self.speed_lebel_3)

        self.movespe_textEdit_longtime = QTextEdit(Dialog)
        self.movespe_textEdit_longtime.setObjectName(u"movespe_textEdit_longtime")
        self.movespe_textEdit_longtime.setMaximumSize(QSize(104, 31))

        self.horizontalLayout_9.addWidget(self.movespe_textEdit_longtime)

        self.speed_lebel_4 = QLabel(Dialog)
        self.speed_lebel_4.setObjectName(u"speed_lebel_4")
        self.speed_lebel_4.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_9.addWidget(self.speed_lebel_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.X_lebel = QLabel(Dialog)
        self.X_lebel.setObjectName(u"X_lebel")
        self.X_lebel.setMaximumSize(QSize(21, 51))

        self.horizontalLayout.addWidget(self.X_lebel)

        self.mouX_textEdit = QTextEdit(Dialog)
        self.mouX_textEdit.setObjectName(u"mouX_textEdit")
        self.mouX_textEdit.setMaximumSize(QSize(104, 31))

        self.horizontalLayout.addWidget(self.mouX_textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Y_lebel = QLabel(Dialog)
        self.Y_lebel.setObjectName(u"Y_lebel")
        self.Y_lebel.setMaximumSize(QSize(21, 51))

        self.horizontalLayout_2.addWidget(self.Y_lebel)

        self.mouY_textEdit = QTextEdit(Dialog)
        self.mouY_textEdit.setObjectName(u"mouY_textEdit")
        self.mouY_textEdit.setMaximumSize(QSize(104, 31))

        self.horizontalLayout_2.addWidget(self.mouY_textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.speed_lebel = QLabel(Dialog)
        self.speed_lebel.setObjectName(u"speed_lebel")
        self.speed_lebel.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_3.addWidget(self.speed_lebel)

        self.movespe_textEdit = QTextEdit(Dialog)
        self.movespe_textEdit.setObjectName(u"movespe_textEdit")
        self.movespe_textEdit.setMaximumSize(QSize(104, 31))

        self.horizontalLayout_3.addWidget(self.movespe_textEdit)

        self.speed_lebel_2 = QLabel(Dialog)
        self.speed_lebel_2.setObjectName(u"speed_lebel_2")
        self.speed_lebel_2.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_3.addWidget(self.speed_lebel_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.mou_move = QPushButton(Dialog)
        self.mou_move.setObjectName(u"mou_move")

        self.verticalLayout.addWidget(self.mou_move)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.speed_lebel_keyboard = QLabel(Dialog)
        self.speed_lebel_keyboard.setObjectName(u"speed_lebel_keyboard")
        self.speed_lebel_keyboard.setMaximumSize(QSize(71, 51))

        self.horizontalLayout_8.addWidget(self.speed_lebel_keyboard)

        self.movespe_textEdit_keyboard = QTextEdit(Dialog)
        self.movespe_textEdit_keyboard.setObjectName(u"movespe_textEdit_keyboard")
        self.movespe_textEdit_keyboard.setMaximumSize(QSize(104, 31))

        self.horizontalLayout_8.addWidget(self.movespe_textEdit_keyboard)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.keyboard_input = QPushButton(Dialog)
        self.keyboard_input.setObjectName(u"keyboard_input")

        self.verticalLayout.addWidget(self.keyboard_input)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LClick_checkBox = QCheckBox(Dialog)
        self.LClick_checkBox.setObjectName(u"LClick_checkBox")

        self.horizontalLayout_4.addWidget(self.LClick_checkBox)

        self.douClick_checkBox = QCheckBox(Dialog)
        self.douClick_checkBox.setObjectName(u"douClick_checkBox")

        self.horizontalLayout_4.addWidget(self.douClick_checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.mou_click = QPushButton(Dialog)
        self.mou_click.setObjectName(u"mou_click")

        self.verticalLayout_2.addWidget(self.mou_click)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"QListView{\n"
"	font: 12pt \"Arial\";\n"
"  color : White;\n"
"}")

        self.verticalLayout_4.addWidget(self.listView)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.up_pushButton = QPushButton(Dialog)
        self.up_pushButton.setObjectName(u"up_pushButton")

        self.horizontalLayout_6.addWidget(self.up_pushButton)

        self.dow_pushButton = QPushButton(Dialog)
        self.dow_pushButton.setObjectName(u"dow_pushButton")

        self.horizontalLayout_6.addWidget(self.dow_pushButton)

        self.del_pushButton = QPushButton(Dialog)
        self.del_pushButton.setObjectName(u"del_pushButton")

        self.horizontalLayout_6.addWidget(self.del_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.record_realtime_button = QPushButton(Dialog)
        self.record_realtime_button.setObjectName(u"record_realtime_button")

        self.verticalLayout_4.addWidget(self.record_realtime_button)

        self.GO_pushbutton = QPushButton(Dialog)
        self.GO_pushbutton.setObjectName(u"GO_pushbutton")

        self.verticalLayout_4.addWidget(self.GO_pushbutton)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u73fe\u5728\u6ed1\u9f20\u4f4d\u7f6e", None))
        self.MOUXY_label.setText("")
        self.speed_lebel_3.setText(QCoreApplication.translate("Dialog", u"\u52d5\u4f5c\u9593\u683c", None))
        self.movespe_textEdit_longtime.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft JhengHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.1</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.speed_lebel_4.setText(QCoreApplication.translate("Dialog", u"\u79d2", None))
        self.X_lebel.setText(QCoreApplication.translate("Dialog", u"X:", None))
        self.Y_lebel.setText(QCoreApplication.translate("Dialog", u"Y:", None))
        self.speed_lebel.setText(QCoreApplication.translate("Dialog", u"\u79fb\u52d5\u901f\u5ea6:", None))
        self.speed_lebel_2.setText(QCoreApplication.translate("Dialog", u"\u79d2", None))
        self.mou_move.setText(QCoreApplication.translate("Dialog", u"\u6ed1\u9f20\u79fb\u52d5", None))
        self.speed_lebel_keyboard.setText(QCoreApplication.translate("Dialog", u"\u9375\u76e4\u8f38\u5165", None))
        self.keyboard_input.setText(QCoreApplication.translate("Dialog", u"\u9375\u76e4\u8f38\u5165", None))
        self.LClick_checkBox.setText(QCoreApplication.translate("Dialog", u"\u5de6\u9375", None))
        self.douClick_checkBox.setText(QCoreApplication.translate("Dialog", u"\u9023\u64ca", None))
        self.mou_click.setText(QCoreApplication.translate("Dialog", u"\u6ed1\u9f20\u9ede\u64ca", None))
        self.up_pushButton.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u79fb", None))
        self.dow_pushButton.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u79fb", None))
        self.del_pushButton.setText(QCoreApplication.translate("Dialog", u"\u522a\u9664", None))
        self.record_realtime_button.setText(QCoreApplication.translate("Dialog", u"\u5373\u6642\u9304\u88fd", None))
        self.GO_pushbutton.setText(QCoreApplication.translate("Dialog", u"F9 \u57f7\u884c", None))
    # retranslateUi

