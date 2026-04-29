from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class TVRemoteView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TV Remote")
        self.resize(900, 600)

        self.screen = QLabel("TV OFF")
        self.screen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.screen.setStyleSheet("background: black; color: white; font-size: 30px")
        self.screen.setFixedSize(550, 300)

        self.power_btn = QPushButton("Power")
        self.channel_up_btn = QPushButton("Channel Up")
        self.channel_down_btn = QPushButton("Channel Down")
        self.volume_up_btn = QPushButton("Volume Up")
        self.volume_down_btn = QPushButton("Volume Down")
        self.mute_btn = QPushButton("Mute")

        self.num_buttons = []
        num_grid = QGridLayout()
        for i in range(6):
            btn = QPushButton(str(i + 1))
            self.num_buttons.append(btn)
            num_grid.addWidget(btn, i // 3, i % 3)

        self.volume_bar = QProgressBar()
        self.volume_bar.setRange(0, 100)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.power_btn)
        left_layout.addLayout(num_grid)
        left_layout.addWidget(self.volume_up_btn)
        left_layout.addWidget(self.volume_down_btn)
        left_layout.addWidget(self.channel_up_btn)
        left_layout.addWidget(self.channel_down_btn)
        left_layout.addWidget(self.mute_btn)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.screen)
        right_layout.addWidget(self.volume_bar)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

    def show_channel(self, image_path):
        pixmap = QPixmap(image_path)
        self.screen.setPixmap(pixmap.scaled(self.screen.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def show_off(self):
        self.screen.setPixmap(QPixmap())
        self.screen.setText("TV OFF")
