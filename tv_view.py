from PyQt6.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QGridLayout,QProgressBar
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class TVRemoteView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TV Remote")
        self.resize(900,600)

        self.screen=QLabel("TV OFF")
        self.screen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.screen.setStyleSheet("background:black;color:white;font-size:30px")
        self.screen.setFixedSize(550,300)

        self.power=QPushButton("Power")
        self.cu=QPushButton("Channel Up")
        self.cd=QPushButton("Channel Down")
        self.vu=QPushButton("Volume Up")
        self.vd=QPushButton("Volume Down")
        self.mute=QPushButton("Mute")

        self.nums=[]
        grid=QGridLayout()
        for i in range(6):
            b=QPushButton(str(i+1))
            self.nums.append(b)
            grid.addWidget(b,i//3,i%3)

        self.bar=QProgressBar()
        self.bar.setRange(0,100)

        left=QVBoxLayout()
        left.addWidget(self.power)
        left.addLayout(grid)
        left.addWidget(self.vu)
        left.addWidget(self.vd)
        left.addWidget(self.cu)
        left.addWidget(self.cd)
        left.addWidget(self.mute)

        right=QVBoxLayout()
        right.addWidget(self.screen)
        right.addWidget(self.bar)

        main=QHBoxLayout()
        main.addLayout(left)
        main.addLayout(right)
        self.setLayout(main)

    def setimg(self,p):
        pix=QPixmap(p)
        self.screen.setPixmap(pix.scaled(self.screen.size(),Qt.AspectRatioMode.KeepAspectRatio))

    def off(self):
        self.screen.setPixmap(QPixmap())
        self.screen.setText("TV OFF")
