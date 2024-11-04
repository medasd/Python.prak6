import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример сигналов и слотов")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Нажмите кнопку", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 16))

        self.button = QPushButton("Нажми меня", self)
        self.button.setStyleSheet("background-color: lightblue; font-size: 14px;")
        
        self.button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_clicked(self):
        self.label.setText("Кнопка нажата!")
        self.label.setStyleSheet("color: green; font-size: 20px;")
        self.button.setStyleSheet("background-color: yellow; font-size: 16px;")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
