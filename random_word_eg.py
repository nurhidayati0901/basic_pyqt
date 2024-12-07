from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice
from PyQt5.QtGui import QPalette, QColor

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Test Window")
main_window.resize(500, 400)

# App Objects
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

my_words = ["Swift", "Ignis", 'Brezza', "Grand Vitara", "Scorpio", "Scorpio N", "Hector", "Harrier", "Innova", "Innova Hycross", "Fortuner", "Legender", "Range Rover", "Defender", "G-Wagon", "Urus", "Aventador", "Mclaren", "Rolls Royce Ghost"]

# Set button colors
button1.setStyleSheet("background-color: white; color: grey; font-size: 16px;")
button2.setStyleSheet("background-color: white; color: grey; font-size: 16px;")
button3.setStyleSheet("background-color: white; color: grey; font-size: 16px;")

# Set label text size
title.setStyleSheet("font-size: 24px; color: white;")
text1.setStyleSheet("font-size: 18px; color: white;")
text2.setStyleSheet("font-size: 18px; color: white;")
text3.setStyleSheet("font-size: 18px; color: white;")

# App design
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Adding Objects
row1.addWidget(title, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Set the background color of the window to black
main_window.setStyleSheet("background-color: black; color: white;")

# Adding Functions
def random_words1():
    words = choice(my_words)
    text1.setText(words)

def random_words2():
    words = choice(my_words)
    text2.setText(words)

def random_words3():
    words = choice(my_words)
    text3.setText(words)

# Events
button1.clicked.connect(random_words1)
button2.clicked.connect(random_words2)
button3.clicked.connect(random_words3)

# Execute App
main_window.show()
app.exec_()