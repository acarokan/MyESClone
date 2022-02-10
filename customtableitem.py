from PySide6.QtWidgets import QTreeWidgetItem
from vlc import Media, MediaList
from audio import Audio


class CustomItem(QTreeWidgetItem, Audio):
    def __init__(self, file):
        Audio.__init__(self, file)
        QTreeWidgetItem.__init__(self)
        self.media = Media(file)


class CustomListItem(QTreeWidgetItem):
    def __init__(self):
        QTreeWidgetItem.__init__(self)
        self.media_list = MediaList()


if __name__ == "__main__":

    cti = CustomItem("C:/Users/droka/Desktop/Programlar/MyESClone/assets/deneme.mp3")