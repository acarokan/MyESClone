import mutagen
from math import ceil
from pymediainfo import MediaInfo
from external import External


class Audio:
    external = External()
    def __init__(self, file):
        self.mi = MediaInfo.parse(file).tracks[0]
        self.play_list = None
        self.parent_str = ""
        self.position = 0
        self.file_dir = self.mi.complete_name
        self.extension = self.mi.file_extension
        self.filename = self.mi.file_name
        try:
            self.duration = self.mi.other_duration[-1]
            self.performer = self.mi.performer
        except:
            file_mutagen = mutagen.File(file).info
            self.duration = self.external.position_converter(ceil(file_mutagen.length)*1000)
            self.performer = None

        self.last_modification_date = self.mi.file_last_modification_date__local.split(" ")[0]
        self.last_modification_time = self.mi.file_last_modification_date__local.split(" ")[-1]

if __name__ == "__main__":

    cti = Audio(r"C:\Users\droka\Desktop\WhatsApp Audio 2022-01-26 at 08.51.54\29 Oca 03.31_.aac")