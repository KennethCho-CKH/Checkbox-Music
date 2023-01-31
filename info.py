import sys
from PyQt5.QtWidgets import QScrollArea, QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(1000, 750)
window.setWindowTitle("App Info")

label = QLabel("""This is a Python program created by Kenneth Kai Hung Cho, designed as a beat maker application. It uses the PyQt5 library for its GUI interface and allows users to:

- create beat patterns
- play the created beat patterns
- save the created beat patterns
- load previously saved beat patterns

The program provides the user with checkboxes to make a beat pattern and buttons for other functionalities mentioned above. The sounds used in the beat patterns include kick, snare, clap, and hihat.

The beats can be exported in MP3 format and saved patterns can be stored as a pickle file.

Please note, this program is currently in beta testing. It is still being developed and improved, but is available for use.""")

label.setAlignment(Qt.AlignLeft)
label.setWordWrap(True)

font = QFont("Poppins")
label.setFont(font)

layout = QVBoxLayout()
layout.addWidget(label)

central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()

sys.exit(app.exec_())
