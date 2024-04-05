

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1330, 667)
        MainWindow.setStyleSheet("background-color: rgb(254, 205, 166);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 1411, 661))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox_8)
        self.groupBox_4.setGeometry(QtCore.QRect(670, 20, 611, 611))
        # self.groupBox_4.setGeometry(QtCore.QRect(10, 190, 541, 441))
        # self.groupBox.setGeometry(QtCore.QRect(670, 20, 611, 611))
        self.groupBox_4.setObjectName("groupBox_4")
        self.adjacency_matrix_out = QtWidgets.QTableWidget(parent=self.groupBox_4)
        self.adjacency_matrix_out.setGeometry(QtCore.QRect(10, 20, 590, 580))
        self.adjacency_matrix_out.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adjacency_matrix_out.setObjectName("adjacency_matrix_out")
        self.adjacency_matrix_out.setColumnCount(0)
        self.adjacency_matrix_out.setRowCount(0)
        self.adjacency_matrix_out.horizontalHeader().setStretchLastSection(False)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_8)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 651, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.groupBox_3)
        self.splitter_2.setGeometry(QtCore.QRect(10, 121, 631, 30))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.im = QtWidgets.QPushButton(parent=self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.im.setFont(font)
        self.im.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.im.setObjectName("im")
        self.widget = QtWidgets.QWidget(parent=self.splitter_2)
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.impulse_modeling_steps = QtWidgets.QSpinBox(parent=self.widget)
        self.impulse_modeling_steps.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.impulse_modeling_steps.setMinimum(1)
        self.impulse_modeling_steps.setMaximum(100)
        self.impulse_modeling_steps.setProperty("value", 10)
        self.impulse_modeling_steps.setObjectName("impulse_modeling_steps")
        self.gridLayout_6.addWidget(self.impulse_modeling_steps, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(parent=self.groupBox_3)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 631, 95))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(parent=self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.input_filename = QtWidgets.QLineEdit(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_filename.setFont(font)
        self.input_filename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_filename.setText("")
        self.input_filename.setPlaceholderText("")
        self.input_filename.setClearButtonEnabled(False)
        self.input_filename.setObjectName("input_filename")
        self.gridLayout.addWidget(self.input_filename, 0, 0, 1, 1)
        self.output_filename = QtWidgets.QLineEdit(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_filename.setFont(font)
        self.output_filename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_filename.setText("")
        self.output_filename.setPlaceholderText("")
        self.output_filename.setClearButtonEnabled(False)
        self.output_filename.setObjectName("output_filename")
        self.gridLayout.addWidget(self.output_filename, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.browse_input = QtWidgets.QToolButton(parent=self.widget1)
        self.browse_input.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.browse_input.setObjectName("browse_input")
        self.gridLayout_2.addWidget(self.browse_input, 0, 0, 1, 1)
        self.browse_output = QtWidgets.QToolButton(parent=self.widget1)
        self.browse_output.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.browse_output.setObjectName("browse_output")
        self.gridLayout_2.addWidget(self.browse_output, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.load_am = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load_am.setFont(font)
        self.load_am.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.load_am.setObjectName("load_am")
        self.gridLayout_5.addWidget(self.load_am, 0, 0, 1, 1)
        self.save_am = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_am.setFont(font)
        self.save_am.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.save_am.setObjectName("save_am")
        self.gridLayout_5.addWidget(self.save_am, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.plot_graph_button = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plot_graph_button.setFont(font)
        self.plot_graph_button.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.plot_graph_button.setObjectName("plot_graph_button")
        self.verticalLayout.addWidget(self.plot_graph_button)
        self.check_stability_button = QtWidgets.QPushButton(parent=self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_stability_button.setFont(font)
        self.check_stability_button.setStyleSheet("background-color: rgb(170, 255, 200);")
        self.check_stability_button.setObjectName("check_stability_button")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.groupBox_8)
        # self.groupBox_9.setGeometry(QtCore.QRect(560, 190, 101, 441))
        self.groupBox_9.setGeometry(QtCore.QRect(670 + 620, 20, 101, 611))
        # self.groupBox_4.setGeometry(QtCore.QRect(670, 20, 611, 611))
        self.groupBox_9.setObjectName("groupBox_9")
        self.q_table = QtWidgets.QTableWidget(parent=self.groupBox_9)
        self.q_table.setGeometry(QtCore.QRect(10, 20, 81, 580))
        self.q_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.q_table.setObjectName("q_table")
        self.q_table.setColumnCount(0)
        self.q_table.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(parent=self.groupBox_8)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 651, 451))
        # self.groupBox_4.setGeometry(QtCore.QRect(10, 190, 541, 441))
        # self.groupBox.setGeometry(QtCore.QRect(670, 20, 611, 611))
        self.groupBox.setObjectName("groupBox")
        self.output_field = QtWidgets.QTextBrowser(parent=self.groupBox)
        self.output_field.setGeometry(QtCore.QRect(10, 20, 634, 420))
        self.output_field.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_field.setObjectName("output_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бригада №6. Робота 6."))
        self.groupBox_8.setTitle(_translate("MainWindow", "Когнітивний аналіз та імпульсне моделювання"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Матриця когнітивної карти"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Дані"))
        self.im.setText(_translate("MainWindow", "Застосувати імпульс"))
        self.label_6.setText(_translate("MainWindow", "Кількість моделюючих кроків :"))
        self.label.setText(_translate("MainWindow", "Input file"))
        self.label_2.setText(_translate("MainWindow", "Output file"))
        self.browse_input.setText(_translate("MainWindow", "..."))
        self.browse_output.setText(_translate("MainWindow", "..."))
        self.load_am.setText(_translate("MainWindow", "Відобразити Матрицю"))
        self.save_am.setText(_translate("MainWindow", "Зберегти матрицю"))
        self.plot_graph_button.setText(_translate("MainWindow", "Відмалювати"))
        self.check_stability_button.setText(_translate("MainWindow", "Перевірити стабільність"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Q-імпульс"))
        self.groupBox.setTitle(_translate("MainWindow", "Результат"))
