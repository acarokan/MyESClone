from PySide6.QtWidgets import QTreeWidget
from PySide6 import QtCore


class CustomQTreeWidget(QTreeWidget):
    fileDropped = QtCore.Signal(list)

    def __init__(self, layout):
        super().__init__(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file = event.mimeData().urls()[0].toLocalFile()
        self.fileDropped.emit([file])
