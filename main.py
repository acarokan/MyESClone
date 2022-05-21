from asyncore import write
import threading
import itertools
import vlc
import os
import shutil
import json
from pathlib import Path
from PySide6.QtCore import QTimer, QSettings, QModelIndex
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog
from template import Ui_MainWindow
from progres_bar import Ui_dialog
from  message_dialog_for_not_file import Ui_Dialog as FileNotUi_Dialog
from customtableitem import CustomItem, CustomListItem
from external import External
from db import DB
from pynput.keyboard import Key, Listener, KeyCode
from pynput import keyboard
from filenamedialog import FileNameDialog
from qt_material import apply_stylesheet
import qtawesome


class ProgressBar(QDialog):
    def __init__(self):
        super(ProgressBar, self).__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ui.progressBar.valueChanged.connect(self.value_change)

    def value_change(self, value):
        if value == self.ui.progressBar.maximum():
            self.close()

    def closeEvent(self, close):
        self.ui.progressBar.setValue(0)


class FileNotDialog(QDialog):
    def __init__(self):
        super(FileNotDialog, self).__init__()
        self.ui = FileNotUi_Dialog()
        self.ui.setupUi(self)

    def set_theme(self, theme):
        invert = True if theme.startswith("light") else False
        apply_stylesheet(self, theme=theme, invert_secondary=invert)
        stylesheet = self.styleSheet()
        with open('css/custom.css') as file:
            app.setStyleSheet(stylesheet + file.read().format(**os.environ))



class Main(QMainWindow):
    mp_vlc = vlc.MediaPlayer()
    media_list_player = vlc.MediaListPlayer()
    mp_vlc_list = media_list_player.get_media_player()
    mp_vlc_event_manager = mp_vlc.event_manager()
    mp_vlc_list_event_manager = mp_vlc_list.event_manager()
    media_list_player_event_manager = media_list_player.event_manager()
    media_player = mp_vlc
    database = DB()

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_application_other_object()
        self.set_application_variable()
        self.set_application_timers()
        self.program_start_with_sound()
        self.connect_signal()
        self.media_player_event_attach()
        self.set_setting_theme_list()
        self.set_settings_before_run()
        self.set_media_before_running()
        self.set_keyboard_listener()

    def set_application_other_object(self):
        self.external = External()
        self.progress_bar = ProgressBar()
        self.file_dialog = QFileDialog()
        self.file_not_dialog = FileNotDialog()
        self.file_dialog.setFileMode(QFileDialog.Directory)

    def set_application_timers(self):
        self.timer = threading.Timer(self.oto_play_time/1000, self.play_after_typing)
        self.timer_rewind = QTimer()
        self.timer_rewind.setInterval(External.get_from_settings_or_defaults("timer_rewind_interval"))
        self.timer_rewind.timeout.connect(self.rewind)

    def set_keyboard_listener(self):
        self.listener = Listener(on_press=self.key_control_press,
                                 on_release=self.key_control_release)
        self.listener.start()
        self.hotkey_listener = keyboard.GlobalHotKeys({
            '<alt>++': self.volume_up_with_key,
            '<alt>+-': self.volume_down_with_key})
        self.hotkey_listener.start()

    def media_player_event_attach(self):
        self.mp_vlc_event_manager.event_attach(vlc.EventType.MediaPlayerLengthChanged,
                                               self.refresh_duration_slider)
        self.mp_vlc_event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged,
                                               self.tick_duration_slider)
        self.mp_vlc_event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,
                                               self.tick_duration_slider_stop)
        self.mp_vlc_list_event_manager.event_attach(vlc.EventType.MediaPlayerLengthChanged,
                                                    self.refresh_duration_slider)
        self.mp_vlc_list_event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged,
                                                    self.tick_duration_slider)
        self.mp_vlc_list_event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,
                                                    self.tick_duration_slider_stop)
        self.media_list_player_event_manager.event_attach(vlc.EventType.MediaListPlayerNextItemSet,
                                                          self.next_item_set)

    def connect_signal(self):
        self.ui.play_button.clicked.connect(self.play)
        self.ui.stop_button.clicked.connect(self.stop)
        self.ui.horizontalSlider.sliderReleased.connect(self.slider_manuel_control_released)
        self.ui.horizontalSlider.sliderPressed.connect(self.slider_manuel_control_pressed)
        self.ui.horizontalSlider.sliderMoved.connect(self.slider_manuel_control_mooved)
        self.ui.treeWidget.itemDoubleClicked.connect(self.play)
        self.ui.volumeScrollBar.valueChanged.connect(self.mp_volume_change)
        self.ui.speedScrollBar.valueChanged.connect(self.mp_speed_change)
        self.ui.share_button.clicked.connect(self.create_shared_object)
        self.ui.go_to_start_button.clicked.connect(self.previous_play)
        self.ui.go_to_end_button.clicked.connect(self.next_play)
        self.ui.rewind_button.pressed.connect(self.rewind_with_button)
        self.ui.fast_forward_button.pressed.connect(self.fast_forward)
        self.ui.rewind_button.released.connect(self.rewind_released_with_button)
        self.ui.fast_forward_button.released.connect(self.fast_forward_released)
        self.ui.file_remove_button.clicked.connect(self.remove_audio)
        self.ui.treeWidget.fileDropped.connect(self.add_file)
        self.ui.theme_list_combo_box.currentTextChanged.connect(self.set_theme)
        self.ui.oto_stop_radio_button_true.toggled.connect(self.oto_stop_toggle)
        self.ui.oto_stop_radio_button_false.toggled.connect(self.oto_stop_toggle)
        self.ui.oto_rewind_spin_box.valueChanged.connect(self.oto_rewind_value_change)
        self.ui.rewind_spin_box.valueChanged.connect(self.rewind_value_change)
        self.ui.volume_combo_box.currentTextChanged.connect(self.volume_step_change)
        self.ui.speed_combo_box.currentTextChanged.connect(self.speed_step_change)
        self.ui.forward_combo_box.currentTextChanged.connect(self.forward_count_change)
        self.ui.oto_play_time_spin_box.valueChanged.connect(self.oto_play_time_change)
        self.ui.keyboard_volume_spin_box.valueChanged.connect(self.volume_step_with_keyboard_change)
        self.ui.file_add_button.clicked.connect(self.add_file_with_button)
        self.ui.add_folder_button.clicked.connect(self.add_folder_with_button)

    def set_application_variable(self):
        self.icons = External.icon_pack()
        self.playing_object = External.get_from_settings_or_defaults("playing_object")
        self.playing_list = External.get_from_settings_or_defaults("playing_list")
        self.player_after_type = External.get_from_settings_or_defaults("player_after_type")
        self.global_stop = External.get_from_settings_or_defaults("global_stop")
        self.durdurma_duzelt = External.get_from_settings_or_defaults("durdurma_duzelt")
        self.oto_stop_toggle_bool = External.get_from_settings_or_defaults("oto_stop_toggle_bool")
        self.rewind_count = External.get_from_settings_or_defaults("rewind_count")
        self.oto_rewind_count = External.get_from_settings_or_defaults("oto_rewind_count")
        self.volume_step = External.get_from_settings_or_defaults("volume_step")
        self.speed_step = External.get_from_settings_or_defaults("speed_step")
        self.forward_count = External.get_from_settings_or_defaults("forward_count")
        self.oto_play_time = External.get_from_settings_or_defaults("oto_play_time")
        self.volume_step_with_keyboard = External.get_from_settings_or_defaults("volume_step_with_keyboard")
        #self.hotkeyup = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>++'), self.volume_up_with_key)
        #self.hotkeydown = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+-'), self.volume_down_with_key)

    def set_media_before_running(self):
        with open("last_sound.json", encoding="UTF-8") as f:
            db = json.load(f)
        media = db["last_sound"]
        if len(media) > 1:
            top_item_num = media[0]
            child_item_num = media[-1]
            topitem = self.ui.treeWidget.topLevelItem(top_item_num)
            childitem = topitem.child(child_item_num)
            self.ui.treeWidget.setCurrentItem(childitem)
        else:
            topitem = self.ui.treeWidget.topLevelItem(media[0])
            self.ui.treeWidget.setCurrentItem(topitem)

        

    def set_settings_before_run(self):
        """
        Bu fonksiyon program çalışmadan önce son yapılan ayarları ayarlar.
        Eğer kayıt defterinde kayıtlı değilse default_settings.json dosyasından çeker.
        """
        self.theme = External.get_from_settings_or_defaults("theme")
        self.set_theme(self.theme)
        self.media_player.audio_set_volume(self.ui.volumeScrollBar.value())
        self.ui.theme_list_combo_box.setCurrentText(self.theme)
        child_gen = iter(self.ui.tab_6.children())
        for child in child_gen:
            if child.property("setVariable"):
                if child.__class__.__name__ == "QSpinBox":
                    child.setValue(External.get_from_settings_or_defaults(child.property("setVariable")))
                elif child.__class__.__name__ == "QComboBox":
                    child.setCurrentText(str(External.get_from_settings_or_defaults(child.property("setVariable"))))

        if self.oto_stop_toggle_bool == "true":
            self.ui.oto_stop_radio_button_true.setChecked(True)
            self.oto_stop_toggle_bool = True
        else:
            self.ui.oto_stop_radio_button_false.setChecked(True)
            self.oto_stop_toggle_bool = False

    def oto_play_time_change(self, value):
        self.oto_play_time = value

    def volume_step_with_keyboard_change(self, value):
        self.volume_step_with_keyboard = value

    def forward_count_change(self, text):
        self.forward_count = int(text)

    def speed_step_change(self, text):
        self.speed_step = int(text)
        self.ui.speedScrollBar.setPageStep(self.speed_step)

    def volume_step_change(self, text):
        self.volume_step = int(text)
        self.ui.volumeScrollBar.setPageStep(self.volume_step)

    def rewind_value_change(self, value):
        self.rewind_count = value

    def oto_rewind_value_change(self, value):
        self.oto_rewind_count = value

    def oto_stop_toggle(self, toggle):
        if self.ui.oto_stop_radio_button_true.isChecked():
            self.oto_stop_toggle_bool = True
        elif self.ui.oto_stop_radio_button_false.isChecked():
            self.oto_stop_toggle_bool = False

    def set_theme(self, theme):
        invert = True if theme.startswith("light") else False
        theme = "themes/" + theme if theme in os.listdir("themes") else theme
        apply_stylesheet(app, theme=theme, invert_secondary=invert)
        stylesheet = app.styleSheet()
        with open('css/custom.css') as file:
            app.setStyleSheet(stylesheet + file.read().format(**os.environ))
        self.set_icons()
        self.theme = theme

    def set_setting_theme_list(self):
        theme_list = External.get_theme_list()
        self.ui.theme_list_combo_box.addItems(theme_list)

    def set_icons(self):
        self.ui.play_button.setIcon(qtawesome.icon("mdi6.play",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.stop_button.setIcon(qtawesome.icon("mdi6.stop",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.go_to_start_button.setIcon(qtawesome.icon("mdi6.skip-backward",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.go_to_end_button.setIcon(qtawesome.icon("mdi6.skip-forward",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.rewind_button.setIcon(qtawesome.icon("mdi6.rewind",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.fast_forward_button.setIcon(qtawesome.icon("mdi6.fast-forward",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.share_button.setIcon(qtawesome.icon("mdi6.monitor-share",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.file_add_button.setIcon(qtawesome.icon("mdi6.file-plus",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.file_remove_button.setIcon(qtawesome.icon("mdi6.file-remove",
                                                   color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                   color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))
        self.ui.add_folder_button.setIcon(qtawesome.icon("ri.folder-add-fill",
                                                          color=os.environ["QTMATERIAL_PRIMARYCOLOR"],
                                                          color_active=os.environ["QTMATERIAL_SECONDARYCOLOR"]))

    def previous_play(self):
        current_item = self.ui.treeWidget.currentItem()
        if current_item.parent():
            self.media_list_player.previous()
        else:
            self.media_player.set_time(0)

    def next_play(self):
        current_item = self.ui.treeWidget.currentItem()
        if current_item.parent():
            self.media_list_player.next()
        else:
            self.media_player.set_time(self.media_player.get_length())

    def next_item_set(self, event):
        try:
            parent_item = self.playing_object.parent()
            playing_item = self.media_player.get_media()
            playing_item_index = self.playing_list.index_of_item(playing_item)
            self.playing_object.setSelected(False)
            parent_item.child(playing_item_index).setSelected(True)
            self.playing_object = parent_item.child(playing_item_index)
        except AttributeError:
            pass

    def change_player(self, player):
        self.mp_vlc.stop()
        self.mp_vlc_list.stop()
        self.media_player = player

    def key_control_press(self, key):
        if key == Key.f7:
            self.rewind()
        elif key == Key.f8:
            self.fast_forward()
        elif key == Key.f9:
            if self.durdurma_duzelt != 0:
                self.media_player.set_time(self.durdurma_duzelt)
            self.media_player.set_pause(0)
            self.global_stop = False
        elif key == Key.f4:
            self.durdurma_duzelt = self.media_player.get_time()
            self.media_player.set_pause(1)
            self.global_stop = True
        elif key == Key.alt_l:
            pass
        elif key == KeyCode.from_char("+"):
            pass
        elif key == KeyCode.from_char("-"):
            pass
        elif hasattr(key, "vk") and key.vk == 109:
            pass
        elif hasattr(key, "vk") and key.vk == 107:
            pass
        else:
            self.oto_stop()

    def key_control_release(self, key):
        if key == Key.f7:
            self.rewind_released()
        elif key == Key.f8:
            self.fast_forward_released()
        elif key == Key.f4:
            pass
        elif key == Key.f9:
            pass
        elif hasattr(key, "vk") and key.vk == 109:
            pass
        elif hasattr(key, "vk") and key.vk == 107:
            pass
        elif key == KeyCode.from_char("+"):
            pass
        elif key == KeyCode.from_char("-"):
            pass
        elif key == Key.alt_l:
            pass
        else:
            if not self.timer.is_alive():
                if not self.global_stop and self.oto_stop_toggle_bool:
                    self.timer.start()

    def oto_stop(self):
        if self.oto_stop_toggle_bool:
            self.timer.cancel()
            del self.timer
            self.timer = threading.Timer(self.oto_play_time/1000, self.play_after_typing)
            self.media_player.set_pause(1)
        else:
            pass

    def play_after_typing(self):
        tm = self.media_player.get_time()
        self.media_player.set_time(tm-self.oto_rewind_count)
        self.media_player.set_pause(0)

    def volume_up_with_key(self):
        val = self.ui.volumeScrollBar.value()
        self.ui.volumeScrollBar.setValue(val + self.volume_step_with_keyboard)

    def volume_down_with_key(self):
        val = self.ui.volumeScrollBar.value()
        self.ui.volumeScrollBar.setValue(val - self.volume_step_with_keyboard)

    def fast_forward(self):
        self.media_player.set_rate(self.forward_count)

    def rewind(self):
        self.media_player.set_pause(1)
        val = self.ui.horizontalSlider.value() - self.rewind_count
        self.ui.horizontalSlider.setValue(val)

    def rewind_with_button(self):
        if self.timer_rewind.isActive():
            pass
        else:
            self.timer_rewind.start()

    def fast_forward_released(self):
        self.media_player.set_pause(1)
        self.media_player.set_rate(self.ui.speedScrollBar.value()/100)
        self.media_player.set_pause(0)

    def rewind_released(self):
        self.media_player.set_time(self.ui.horizontalSlider.value())
        self.media_player.set_pause(0)

    def rewind_released_with_button(self):
        self.timer_rewind.stop()
        self.rewind_released()

    def program_start_with_sound(self):

            all_items = self.database.get_all_items()
            for i in reversed(all_items):
                try:
                    if isinstance(i, list):
                        self.add_audio_with_child(i)
                    else:
                        self.add_audio(i)
                except FileNotFoundError as err:
                    err_message = str(err)
                    err_file = os.path.basename(err_message)
                    err_dir = os.path.dirname(err_message)
                    message = "{} isimli dosya {} dizini içinde bulunamadı. \n" \
                              "Dosya veri tabanından çıkarılacak. \n" \
                              "Eğer dosya bir dizin içinde ise ve dizin silinmişse tüm dizin veri tabanından çıkarılacak".format(err_file, err_dir)
                    self.file_not_dialog.set_theme(External.get_from_settings_or_defaults("theme"))
                    self.file_not_dialog.ui.message.setText(message)
                    self.file_not_dialog.exec()

    def write_db_before_close(self):
        db_list = {}
        all_items = self.ui.treeWidget.findItems("", QtCore.Qt.MatchContains, 0)
        for ind, topitem in enumerate(all_items):
            itemcount = topitem.childCount()
            db_child_list = []
            if itemcount > 0:
                for i in range(0, itemcount):
                    item = topitem.child(i)
                    item.parent_str = topitem.text(0)
                    ekle = dict(itertools.islice(item.__dict__.items(), 1, None))
                    ekle.pop("media")
                    db_child_list.append(ekle)
                db_list[str(ind)] = db_child_list
            else:
                ekle = dict(itertools.islice(topitem.__dict__.items(), 1, None))
                ekle.pop("media")
                db_list[str(ind)] = ekle

        self.database.add_item_db(db_list)

    def set_item_position(self):
        self.playing_object.position = self.media_player.get_time()

    def slider_manuel_control_pressed(self):
        self.mp_vlc_event_manager.event_detach(vlc.EventType.MediaPlayerLengthChanged)
        self.mp_vlc_event_manager.event_detach(vlc.EventType.MediaPlayerTimeChanged)
        self.mp_vlc_list_event_manager.event_detach(vlc.EventType.MediaPlayerLengthChanged)
        self.mp_vlc_list_event_manager.event_detach(vlc.EventType.MediaPlayerTimeChanged)

    def slider_manuel_control_released(self):
        pos = self.ui.horizontalSlider.value()
        self.playing_object.position = pos
        self.media_player.set_time(pos)
        self.mp_vlc_event_manager.event_attach(vlc.EventType.MediaPlayerLengthChanged,
                                               self.refresh_duration_slider)
        self.mp_vlc_event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged,
                                               self.tick_duration_slider)
        self.mp_vlc_list_event_manager.event_attach(vlc.EventType.MediaPlayerLengthChanged,
                                                    self.refresh_duration_slider)
        self.mp_vlc_list_event_manager.event_attach(vlc.EventType.MediaPlayerTimeChanged,
                                                    self.tick_duration_slider)

    def slider_manuel_control_mooved(self, pos):
        pos = self.external.position_converter(pos)
        self.ui.label_3.setText(pos)

    def refresh_duration_slider(self, event):
        self.ui.horizontalSlider.setMaximum(self.media_player.get_length())

    def tick_duration_slider(self, event):
        self.ui.horizontalSlider.setValue(self.media_player.get_time())
        self.set_duration_label()
        self.set_item_position()

    def tick_duration_slider_stop(self, event):
        self.ui.horizontalSlider.setValue(self.media_player.get_length())
        self.playing_object.position = 0

    def set_duration_label(self):
        pos = self.external.position_converter(self.media_player.get_time())
        self.ui.label_3.setText(pos)

    def add_audio_with_child(self, file):
        parent_item = CustomListItem()
        parent_item.setText(0, file[0]["parent_str"])
        media_list = parent_item.media_list
        for i in file:
            cti = CustomItem(i["file_dir"])
            cti.play_list = i["play_list"]
            cti.setText(0, i["filename"]),
            cti.setText(1, i["performer"]),
            cti.setText(2, i["last_modification_date"]),
            cti.setText(3, i["last_modification_time"]),
            cti.setText(4, i["duration"])
            cti.position = i["position"]
            parent_item.addChild(cti)
            media_list.add_media(cti.media)
        self.ui.treeWidget.insertTopLevelItem(0, parent_item)

    def add_audio(self, file, name=None):
        if isinstance(file, str):
            cti = CustomItem(file)
            if name:
                cti.setText(0, name)
                cti.filename = name
            else:
                cti.setText(0, cti.filename)
            cti.setText(1, cti.performer)
            cti.setText(2, cti.last_modification_date)
            cti.setText(3, cti.last_modification_time)
            cti.setText(4, cti.duration)
            cti.file_dir = os.path.join("sounds", cti.filename + "." + cti.extension)
            self.ui.treeWidget.insertTopLevelItem(0, cti)
        else:
            cti = CustomItem(file["file_dir"])
            if name:
                cti.setText(0, name)
                cti.filename = name
            else:
                cti.setText(0, file["filename"])
            cti.setText(1, file["performer"])
            cti.setText(2, file["last_modification_date"])
            cti.setText(3, file["last_modification_time"])
            cti.setText(4, file["duration"])
            cti.position = file["position"]
            cti.file_dir = os.path.join("sounds", file["filename"] + "." + file["extension"])
            self.ui.treeWidget.insertTopLevelItem(0, cti)

    def remove_audio(self):
        current_item = self.ui.treeWidget.currentItem()
        if current_item.parent():
            parent = current_item.parent()
            c_index = parent.indexOfChild(current_item)
            parent.takeChild(c_index)
            parent.media_list.remove_index(c_index)
            self.media_list_player.set_media_list(parent.media_list)
            self.playing_list = parent.media_list
            self.media_list_player.play_item_at_index(c_index)
            self.playing_object = self.ui.treeWidget.currentItem()
            file = os.path.join("sounds", parent.text(0))
            file = os.path.join(file, current_item.text(0))
            os.remove(file + "." + current_item.extension)
        else:
            index = self.ui.treeWidget.indexOfTopLevelItem(current_item)
            self.ui.treeWidget.takeTopLevelItem(index)
            self.media_player.stop()
            file = os.path.join("sounds", current_item.text(0))
            if current_item.childCount() > 0:
                shutil.rmtree(file)
            else:
                try:
                    os.remove(file + "." + current_item.extension)
                except:
                    pass
                try:
                    os.rmdir(file)
                except:
                    pass
        self.write_db_before_close()

    def add_audios(self, file, name=None):
        cti = CustomListItem()
        if name:
            cti.setText(0, name)
        else:
            cti.setText(0, os.path.basename(file))
        for root, dirs, files in os.walk(file):
            for i in files:
                path = os.path.join(root, i)
                subcti = CustomItem(path)
                subcti.setText(0, subcti.filename),
                subcti.setText(1, subcti.performer),
                subcti.setText(2, subcti.last_modification_date),
                subcti.setText(3, subcti.last_modification_time),
                subcti.setText(4, subcti.duration)
                base_path = os.path.join("sounds", cti.text(0))
                subcti.file_dir = os.path.join(base_path, subcti.filename + "." + subcti.extension)
                cti.addChild(subcti)
                cti.media_list.add_media(subcti.media)
        self.ui.treeWidget.insertTopLevelItem(0, cti)

    def add_file(self, file):
        all_items = self.ui.treeWidget.findItems("", QtCore.Qt.MatchContains, 0)
        all_names = [i.text(0) for i in all_items]
        file = file[0] if isinstance(file, list) else file
        name = self.external.set_new_name(all_names, Path(file).stem)
        file = self.external.copy_file_in_sounds_dir(file, name, self.progress_bar.ui.progressBar)
        self.progress_bar.exec()
        self.external.convert_thread.join()
        
        file_is_dir = os.path.isdir(file)
        self.add_audios(file, name) if file_is_dir else self.add_audio(file, name)
        self.write_db_before_close()

    def add_file_with_button(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_path = file_dialog.getOpenFileUrl()[0].path().lstrip("/")
        self.add_file(file_path) if file_path else ""
        del file_dialog

    def add_folder_with_button(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)
        folder_path = file_dialog.getExistingDirectoryUrl().path().lstrip("/")
        self.add_file(folder_path) if folder_path else ""

    def play(self):
        self.global_stop = False
        item = self.ui.treeWidget.currentItem()
        parent = item.parent()
        self.playing_object = item
        if parent:
            self.change_player(self.mp_vlc_list)
            item_index = item.parent().indexOfChild(item)
            self.media_list_player.set_media_list(parent.media_list)
            self.playing_list = parent.media_list
            self.media_list_player.play_item_at_index(item_index)
            self.media_player.set_time(self.playing_object.position)
        else:
            self.change_player(self.mp_vlc)
            self.media_player.set_media(item.media)
            self.media_player.play()
            self.media_player.set_time(self.playing_object.position)

    def stop(self):
        self.global_stop = True
        self.media_player.set_pause(1)

    def mp_volume_change(self, val):
        self.media_player.audio_set_volume(val)
        self.mp_vlc.audio_set_volume(val)
        self.mp_vlc_list.audio_set_volume(val)
        self.ui.volume_label.setText("Volume: " + str(val))

    def mp_speed_change(self, val):
        self.media_player.set_pause(1)
        self.media_player.set_rate(val / 100)
        self.mp_vlc.set_rate(val / 100)
        self.mp_vlc_list.set_rate(val / 100)
        self.media_player.set_pause(0)
        self.ui.speed_label.setText("Speed: %" + str(val))

    def create_shared_object(self):
        self.file_dialog.setFileMode(QFileDialog.Directory)
        self.global_stop = True
        self.media_player.set_pause(1)
        file_path = self.ui.treeWidget.currentItem().file_dir
        save_path = self.file_dialog.getExistingDirectoryUrl().path().lstrip("/") + "/"
        start_sn = self.media_player.get_time()
        fnd = FileNameDialog()
        fnd.exec()
        filename = fnd.filename
        sn = int(fnd.sn)
        del fnd
        self.external.cut_sound_thread = threading.Thread(target=self.external.cut_sound,
                                                          args=(file_path, save_path, filename, start_sn, sn,))
        self.external.cut_sound_thread.start()
        self.media_player.set_pause(0)

    def save_settings_before_close(self):
        setting = QSettings("MyESClone", "player")
        setting.setValue("oto_rewind_count", self.oto_rewind_count)
        setting.setValue("theme", self.theme)
        setting.setValue("oto_stop_toggle_bool", self.oto_stop_toggle_bool)
        setting.setValue("rewind_count", self.rewind_count)
        setting.setValue("volume_step", self.volume_step)
        setting.setValue("speed_step", self.speed_step)
        setting.setValue("forward_count", self.forward_count)
        setting.setValue("oto_play_time", self.oto_play_time)
        setting.setValue("volume_step_with_keyboard", self.volume_step_with_keyboard)

    def get_last_play_sound(self):

        data = []
        top_num = -1
        child_num = -1
        last_play = self.ui.treeWidget.currentItem()
        last_play_parent = last_play.parent()
        if last_play_parent:
            top_num = self.ui.treeWidget.indexOfTopLevelItem(last_play_parent)
            child_num = last_play_parent.indexOfChild(last_play)
            data = [top_num, child_num]
        else:
            top_num = self.ui.treeWidget.indexOfTopLevelItem(last_play)
            data = [top_num]

        data = {
            "last_sound": data
        }
        with open("last_sound.json","w", encoding="UTF-8") as f:
            json.dump(data,f,indent=4)
            

    def closeEvent(self, arg):
        self.write_db_before_close()
        self.save_settings_before_close()
        self.get_last_play_sound()


if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
