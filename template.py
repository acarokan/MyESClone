# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from customqtreewidget import CustomQTreeWidget
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QRadioButton,
    QScrollBar, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(678, 507)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(False)
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.menu_bar = QHBoxLayout()
        self.menu_bar.setObjectName(u"menu_bar")
        self.add_folder_button = QPushButton(self.tab_5)
        self.add_folder_button.setObjectName(u"add_folder_button")
        self.add_folder_button.setIconSize(QSize(32, 32))

        self.menu_bar.addWidget(self.add_folder_button)

        self.file_add_button = QPushButton(self.tab_5)
        self.file_add_button.setObjectName(u"file_add_button")
        self.file_add_button.setIconSize(QSize(32, 32))

        self.menu_bar.addWidget(self.file_add_button)

        self.file_remove_button = QPushButton(self.tab_5)
        self.file_remove_button.setObjectName(u"file_remove_button")
        self.file_remove_button.setIconSize(QSize(32, 32))

        self.menu_bar.addWidget(self.file_remove_button)


        self.gridLayout.addLayout(self.menu_bar, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSlider = QSlider(self.tab_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximumSize(QSize(16777215, 100))
#if QT_CONFIG(tooltip)
        self.horizontalSlider.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.horizontalSlider.setToolTipDuration(-2)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(0)
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.play_button = QPushButton(self.tab_5)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.play_button)

        self.stop_button = QPushButton(self.tab_5)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.go_to_start_button = QPushButton(self.tab_5)
        self.go_to_start_button.setObjectName(u"go_to_start_button")
        self.go_to_start_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.go_to_start_button)

        self.rewind_button = QPushButton(self.tab_5)
        self.rewind_button.setObjectName(u"rewind_button")
        self.rewind_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.rewind_button)

        self.fast_forward_button = QPushButton(self.tab_5)
        self.fast_forward_button.setObjectName(u"fast_forward_button")
        self.fast_forward_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.fast_forward_button)

        self.go_to_end_button = QPushButton(self.tab_5)
        self.go_to_end_button.setObjectName(u"go_to_end_button")
        self.go_to_end_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.go_to_end_button)

        self.share_button = QPushButton(self.tab_5)
        self.share_button.setObjectName(u"share_button")
        self.share_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.share_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.formWidget = QWidget(self.tab_5)
        self.formWidget.setObjectName(u"formWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.formWidget.sizePolicy().hasHeightForWidth())
        self.formWidget.setSizePolicy(sizePolicy2)
        self.formWidget.setMinimumSize(QSize(150, 95))
        self.formWidget.setMaximumSize(QSize(150, 100))
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.volume_label = QLabel(self.formWidget)
        self.volume_label.setObjectName(u"volume_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.volume_label)

        self.speed_label = QLabel(self.formWidget)
        self.speed_label.setObjectName(u"speed_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.speed_label)

        self.speedScrollBar = QScrollBar(self.formWidget)
        self.speedScrollBar.setObjectName(u"speedScrollBar")
        self.speedScrollBar.setMouseTracking(False)
        self.speedScrollBar.setLayoutDirection(Qt.LeftToRight)
        self.speedScrollBar.setMinimum(25)
        self.speedScrollBar.setMaximum(300)
        self.speedScrollBar.setSingleStep(25)
        self.speedScrollBar.setPageStep(25)
        self.speedScrollBar.setValue(100)
        self.speedScrollBar.setTracking(True)
        self.speedScrollBar.setOrientation(Qt.Horizontal)
        self.speedScrollBar.setInvertedAppearance(False)
        self.speedScrollBar.setInvertedControls(False)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.speedScrollBar)

        self.volumeScrollBar = QScrollBar(self.formWidget)
        self.volumeScrollBar.setObjectName(u"volumeScrollBar")
        self.volumeScrollBar.setMouseTracking(True)
        self.volumeScrollBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.volumeScrollBar.setLayoutDirection(Qt.LeftToRight)
        self.volumeScrollBar.setAutoFillBackground(False)
        self.volumeScrollBar.setStyleSheet(u"")
        self.volumeScrollBar.setInputMethodHints(Qt.ImhNone)
        self.volumeScrollBar.setMaximum(100)
        self.volumeScrollBar.setValue(50)
        self.volumeScrollBar.setOrientation(Qt.Horizontal)
        self.volumeScrollBar.setInvertedAppearance(False)
        self.volumeScrollBar.setInvertedControls(False)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.volumeScrollBar)


        self.horizontalLayout_4.addWidget(self.formWidget)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.treeWidget = CustomQTreeWidget(self.tab_5)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(0, 270))
        self.treeWidget.setSizeIncrement(QSize(0, 0))
        self.treeWidget.setBaseSize(QSize(0, 0))
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(120)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(True)

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_7 = QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_5 = QFrame(self.tab_6)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 9, 0, 1, 3)

        self.keyboard_volume_spin_box = QSpinBox(self.tab_6)
        self.keyboard_volume_spin_box.setObjectName(u"keyboard_volume_spin_box")
        self.keyboard_volume_spin_box.setMaximum(100)

        self.gridLayout_2.addWidget(self.keyboard_volume_spin_box, 16, 2, 1, 1)

        self.rewind_spin_box = QSpinBox(self.tab_6)
        self.rewind_spin_box.setObjectName(u"rewind_spin_box")
        self.rewind_spin_box.setMaximum(100000)
        self.rewind_spin_box.setValue(1000)

        self.gridLayout_2.addWidget(self.rewind_spin_box, 4, 2, 1, 1)

        self.theme_list_combo_box = QComboBox(self.tab_6)
        self.theme_list_combo_box.setObjectName(u"theme_list_combo_box")

        self.gridLayout_2.addWidget(self.theme_list_combo_box, 0, 2, 1, 1)

        self.volume_combo_box = QComboBox(self.tab_6)
        self.volume_combo_box.addItem("")
        self.volume_combo_box.addItem("")
        self.volume_combo_box.addItem("")
        self.volume_combo_box.addItem("")
        self.volume_combo_box.setObjectName(u"volume_combo_box")

        self.gridLayout_2.addWidget(self.volume_combo_box, 10, 2, 1, 1)

        self.oto_stop_radio_button_false = QRadioButton(self.tab_6)
        self.oto_stop_radio_button_false.setObjectName(u"oto_stop_radio_button_false")

        self.gridLayout_2.addWidget(self.oto_stop_radio_button_false, 2, 2, 1, 1)

        self.oto_rewind_spin_box = QSpinBox(self.tab_6)
        self.oto_rewind_spin_box.setObjectName(u"oto_rewind_spin_box")
        self.oto_rewind_spin_box.setMaximum(100000)
        self.oto_rewind_spin_box.setValue(1000)
        self.oto_rewind_spin_box.setDisplayIntegerBase(10)

        self.gridLayout_2.addWidget(self.oto_rewind_spin_box, 8, 2, 1, 1)

        self.speed_combo_box = QComboBox(self.tab_6)
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.setObjectName(u"speed_combo_box")

        self.gridLayout_2.addWidget(self.speed_combo_box, 12, 2, 1, 1)

        self.label_7 = QLabel(self.tab_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QLabel(self.tab_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.forward_combo_box = QComboBox(self.tab_6)
        self.forward_combo_box.addItem("")
        self.forward_combo_box.addItem("")
        self.forward_combo_box.addItem("")
        self.forward_combo_box.addItem("")
        self.forward_combo_box.setObjectName(u"forward_combo_box")

        self.gridLayout_2.addWidget(self.forward_combo_box, 6, 2, 1, 1)

        self.label_8 = QLabel(self.tab_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1)

        self.oto_stop_radio_button_true = QRadioButton(self.tab_6)
        self.oto_stop_radio_button_true.setObjectName(u"oto_stop_radio_button_true")

        self.gridLayout_2.addWidget(self.oto_stop_radio_button_true, 2, 1, 1, 1)

        self.line = QFrame(self.tab_6)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setStyleSheet(u"")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)

        self.label_4 = QLabel(self.tab_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.line_7 = QFrame(self.tab_6)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 13, 0, 1, 3)

        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 16, 0, 1, 1)

        self.oto_play_time_spin_box = QSpinBox(self.tab_6)
        self.oto_play_time_spin_box.setObjectName(u"oto_play_time_spin_box")
        self.oto_play_time_spin_box.setMaximum(100000)

        self.gridLayout_2.addWidget(self.oto_play_time_spin_box, 14, 2, 1, 1)

        self.label_9 = QLabel(self.tab_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 14, 0, 1, 1)

        self.line_2 = QFrame(self.tab_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 3)

        self.label_6 = QLabel(self.tab_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.line_4 = QFrame(self.tab_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setWindowModality(Qt.WindowModal)
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 7, 0, 1, 3)

        self.label = QLabel(self.tab_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.line_3 = QFrame(self.tab_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setWindowModality(Qt.ApplicationModal)
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 3)

        self.line_6 = QFrame(self.tab_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 0))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 11, 0, 1, 3)

        self.line_8 = QFrame(self.tab_6)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 15, 0, 1, 3)

        self.line_9 = QFrame(self.tab_6)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 17, 0, 1, 3)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyESClone", None))
        self.add_folder_button.setText("")
        self.file_add_button.setText("")
        self.file_remove_button.setText("")
#if QT_CONFIG(statustip)
        self.horizontalSlider.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.play_button.setText("")
        self.stop_button.setText("")
        self.go_to_start_button.setText("")
        self.rewind_button.setText("")
        self.fast_forward_button.setText("")
        self.go_to_end_button.setText("")
        self.share_button.setText("")
        self.volume_label.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
#if QT_CONFIG(statustip)
        self.volumeScrollBar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.volumeScrollBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"S\u00fcre", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Saat", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Tarih", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"G\u00f6nderen", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Dosya Ad\u0131", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Player", None))
        self.line_5.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.keyboard_volume_spin_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"volume_step_with_keyboard", None))
        self.rewind_spin_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"rewind_count", None))
        self.theme_list_combo_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"theme", None))
        self.volume_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.volume_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.volume_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.volume_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"25", None))

        self.volume_combo_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"volume_step", None))
        self.oto_stop_radio_button_false.setText(QCoreApplication.translate("MainWindow", u"Kapal\u0131", None))
        self.oto_rewind_spin_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"oto_rewind_count", None))
        self.speed_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.speed_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.speed_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.speed_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"25", None))

        self.speed_combo_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"speed_step", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ses de\u011fi\u015ftirme miktar\u0131", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Yazarken otomatik durma", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0130leri sarma katsay\u0131s\u0131", None))
        self.forward_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.forward_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.forward_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.forward_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.forward_combo_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"forward_count", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"H\u0131z de\u011fi\u015ftirme miktar\u0131", None))
        self.oto_stop_radio_button_true.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131k", None))
        self.line.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Geri sarma h\u0131z\u0131(milisaniye)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Klavye ile ses de\u011fi\u015ftirme miktar\u0131", None))
        self.oto_play_time_spin_box.setProperty("setVariable", QCoreApplication.translate("MainWindow", u"oto_play_time", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Otomatik oynatma ba\u015flama s\u00fcresi(milisaniye)", None))
        self.line_2.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Otomatik oynatma geri sarma miktar\u0131(milisaniye)", None))
        self.line_4.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tema", None))
        self.line_3.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.line_6.setProperty("class", QCoreApplication.translate("MainWindow", u"ColorLine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Ayarlar", None))
    # retranslateUi

