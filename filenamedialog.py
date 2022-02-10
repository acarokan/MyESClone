from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QGroupBox, QLineEdit, QLabel, QComboBox


class FileNameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.filename = ""
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.accepted.connect(self.set_file_name)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Dosya Adı")
        layout = QtWidgets.QFormLayout()
        self.filename_edit = QLineEdit()
        self.cb = QComboBox()
        self.cb.addItems(["10", "20", "30", "40", "50"])
        layout.addRow(QLabel("Dosya Adı:"), self.filename_edit)
        layout.addRow(QLabel("Kesme Süresi: "), self.cb)
        self.formGroupBox.setLayout(layout)

    def set_file_name(self):
        self.filename = self.filename_edit.text().strip().replace(" ", "_")
        self.sn = self.cb.currentText()