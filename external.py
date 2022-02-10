import json
import os
import shutil
import queue
from threading import Thread
from pydub import AudioSegment
from pathlib import Path
from qt_material import list_themes
from PySide6.QtCore import QSettings


class External:
    def __init__(self):
        self.convert_thread = Thread()
        self.cut_sound_thread = Thread()

    @staticmethod
    def get_theme_list():
        material_themes = list_themes()
        custom_themes = os.listdir("themes")
        all_themes = material_themes + custom_themes
        return all_themes

    @staticmethod
    def get_from_settings_or_defaults(key):
        with open("defaultsettings.json", "r", encoding="utf-8") as f:
            default_settings = json.load(f)
        settings = QSettings("MyESClone", "Player")
        setting = settings.value(key)
        setting = setting if setting else default_settings[key]
        return setting


    @staticmethod
    def icon_pack():
        icons = {}
        #icons["play"] = qta.icon("fa5s.play")
        #icons["stop"] = qta.icon("fa_stop.flag")
        #icons["step_backward"] = qta.icon("fa-step-backward.flag")
        #icons["step_forward"] = qta.icon("fa-step-forward.flag")
        #icons["fast_forward"] = qta.icon("fa-forward.flag")
        #icons["rewind"] = qta.icon("fa-backward.flag")
        #icons["share"] = qta.icon("fa-share-alt.flag")
        #icons["add_file"] = qta.icon("fa-folder-plus.flag")
        #icons["remove_file"] = qta.icon("fa-folder-minus.flag")

        return icons

    def position_converter(self, position):
        sa = "00"
        dk = "00"
        sn = "00"
        kalan = "0"
        sa, kalan = divmod(position, 3600000)
        dk, kalan = divmod(kalan, 60000)
        sn, kalan = divmod(kalan, 1000)
        sonuc = str(sa)+":"+str(dk)+":"+str(sn)
        return sonuc

    def get_extension(self, file):
        ext = Path(file).suffix
        return ext[1:]

    def get_file_name(self, file):
        name = Path(file).stem
        return name

    def convert_wav(self, qu, file_path, name, progress_bar):
        """
        Bu fonksiyon verilen dosyayı wav formatına dönüştürür.
        Eğer bir dizin adresi verilirse dizindeki tüm dosyaları wav formatına dönüştürür
        """
        size = qu.qsize()
        progress_bar.setMaximum(size)
        if os.path.isdir(file_path):
            Path("sounds/"+name).mkdir(parents=True, exist_ok=True)
            while True:
                file = qu.get()
                file_ex = self.get_extension(file)
                new_sound = AudioSegment.from_file(file, file_ex)
                new_sound.export(os.path.join("sounds/"+name, self.get_file_name(file)) + ".wav", format="wav")
                progress_bar.setValue(size - qu.qsize())
                if qu.empty():
                    break
        else:
            size = qu.qsize()
            progress_bar.setMaximum(size)
            file = qu.get()
            file_name = name
            file_ex = self.get_extension(file)
            new_sound = AudioSegment.from_file(file, file_ex)
            new_sound.export("sounds/" + file_name + ".wav", format="wav")
            progress_bar.setValue(size - qu.qsize())
            return "sounds/" + file_name + ".wav"

    def cut_sound(self, file_path, save_path, filename, start_sn, sn):
        save_path = save_path
        start_sn = start_sn
        sn = sn*1000
        file_path = file_path
        file_ex = self.get_extension(file_path)
        new_sound = AudioSegment.from_file(file_path, file_ex)
        new_sound = new_sound[start_sn:start_sn + sn]
        new_sound.export(save_path+filename+".wav", format="wav")

    def set_new_name(self, gen, name):
        count = len(gen)
        iter = 0
        inner_iter = 0
        file_name = name
        while iter < count:
            if file_name == gen[iter]:
                inner_iter +=1
                file_name = name + "({})".format(str(inner_iter))
                iter = 0
            else:
                iter +=1

        return file_name

    def copy_file_in_sounds_dir(self, file_path, name, progress_bar):
        """
        Bu fonksiyon verilen klasör yolundaki klasörü tüm içeriği
        ile ya da dosyanın kendisini sounds adlı dizine kopyalar
        """
        if os.path.isdir(file_path):
            qu = queue.Queue()
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    qu.put(os.path.join(root, file))

            self.convert_thread = Thread(target=self.convert_wav, daemon=True, args=(qu, file_path, name, progress_bar))
            self.convert_thread.start()
            return "sounds/" + name
        else:
            qu = queue.Queue()
            qu.put(file_path)
            self.convert_thread = Thread(target=self.convert_wav, daemon=True, args=(qu, file_path, name, progress_bar))
            self.convert_thread.start()
            return "sounds/" + Path(name).stem+".wav"

    def remove_file_from_sounds_dir(self, file_path, name):
        """
        Bu fonksiyon programdan silinen dosya ve klasörleri sounds dizininden siler.
        """
        if os.path.isdir(file_path):

            shutil.copytree(file_path, "sounds/" + name)
            return "sounds/" + name
        else:
            shutil.copy2(file_path, "sounds/" + name)
            return "sounds/" + name


if __name__ == "__main__":
    print(External().set_new_name(["okan.waw"], "okan"))