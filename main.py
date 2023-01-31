import sys
import os
import time
import pickle
from pydub import AudioSegment
from pydub import AudioSegment
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class BeatMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox Music")
        self.sounds = ["kick.wav", "snare.wav", "clap.wav", "hihat.wav"]
        self.players = [QMediaPlayer() for i in range(len(self.sounds))]
        self.create_widgets()

    def create_widgets(self):
        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.check_boxes = []
        for s, sound in enumerate(self.sounds):
            label = QLabel(sound)
            poppins = QFont("Poppins")
            label.setFont(poppins)
            grid_layout.addWidget(label, s, 0)
            column = []
            for b in range(16):
                check_box = QCheckBox()
                column.append(check_box)
                grid_layout.addWidget(check_box, s, b + 1)
            self.check_boxes.append(column)

        play_export_layout = QHBoxLayout()
        layout.insertLayout(0, play_export_layout)


        self.play_button = QPushButton("Play")
        self.play_button.setFont(poppins)
        self.play_button.clicked.connect(self.play_beat)
        play_export_layout.addWidget(self.play_button)

        self.export_button = QPushButton("Export")
        self.export_button.setFont(poppins)
        self.export_button.clicked.connect(self.export_beat_mp3)
        play_export_layout.addWidget(self.export_button)

        bottom_layout = QHBoxLayout()
        layout.addLayout(bottom_layout)

        self.save_button = QPushButton("Save")
        self.save_button.setFont(poppins)
        self.save_button.clicked.connect(self.save_beat)
        bottom_layout.addWidget(self.save_button)

        self.load_button = QPushButton("Load")
        self.load_button.setFont(poppins)
        self.load_button.clicked.connect(self.load_beat)
        bottom_layout.addWidget(self.load_button)

        self.info_button = QPushButton("Info")
        self.info_button.setFont(poppins)
        self.info_button.clicked.connect(self.open_info)
        bottom_layout.addWidget(self.info_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(poppins)
        self.exit_button.clicked.connect(self.exit_app)
        bottom_layout.addWidget(self.exit_button)
    
    def save_beat(self):
        beat_pattern = []
        for sound in range(len(self.sounds)):
            beat_column = []
            for b in range(16):
                beat_column.append(self.check_boxes[sound][b].isChecked())
            beat_pattern.append(beat_column)
        with open("beat_pattern.pickle", "wb") as f:
            pickle.dump(beat_pattern, f)

    def load_beat(self):
        try:
            with open("beat_pattern.pickle", "rb") as f:
                beat_pattern = pickle.load(f)
                for sound in range(len(self.sounds)):
                    for b in range(16):
                        self.check_boxes[sound][b].setChecked(beat_pattern[sound][b])
        except FileNotFoundError:
            print("No saved beat pattern found.")

    def play_beat(self):
        self.play_button.setEnabled(False)
        row = 0
        while row < 16:
            for sound in range(len(self.sounds)):
                if self.check_boxes[sound][row].isChecked():
                    self.players[sound].setMedia(QMediaContent(QUrl.fromLocalFile(self.sounds[sound])))
                    self.players[sound].play()
            time.sleep(0.125)
            row += 1
        self.play_button.setEnabled(True)
        
    def export_beat_mp3(self):
        pass

    def open_info(self):
        os.system('python info.py')

    def exit_app(self):
        sys.exit()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    beat_maker = BeatMaker()
    beat_maker.show()
    sys.exit(app.exec_())
