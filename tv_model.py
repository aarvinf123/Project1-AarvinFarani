from dataclasses import dataclass

@dataclass
class Channel:
    number:int
    name:str
    image:str

class TVModel:
    def __init__(self):
        self.channels=[
            Channel(1,"News","images/news.jpeg"),
            Channel(2,"Cartoons","images/cartoons.jpeg"),
            Channel(3,"Football","images/football.jpeg"),
            Channel(4,"Basketball","images/basketball.jpeg"),
            Channel(5,"Golf","images/golf.jpeg"),
            Channel(6,"College Basketball","images/college_basketball.jpeg")
        ]
        self.i=0
        self.on=False
        self.v=50
        self.prev=50
        self.muted=False

    def power(self):
        self.on=not self.on

    def cu(self):
        if self.on: self.i=(self.i+1)%len(self.channels)

    def cd(self):
        if self.on: self.i=(self.i-1)%len(self.channels)

    def setc(self,n):
        if self.on and 1<=n<=len(self.channels): self.i=n-1

    def vu(self):
        if self.on and self.v<100:
            self.muted=False
            self.v=min(100,self.v+5)
            self.prev=self.v

    def vd(self):
        if self.on and self.v>0:
            self.muted=False
            self.v=max(0,self.v-5)
            self.prev=self.v

    def mute(self):
        if self.on:
            if self.muted:
                self.muted=False
                self.v=self.prev
            else:
                self.muted=True
                self.prev=self.v
                self.v=0

    def cur(self):
        return self.channels[self.i]
