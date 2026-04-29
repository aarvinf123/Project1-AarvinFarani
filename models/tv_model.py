from dataclasses import dataclass

@dataclass
class Channel:
    number: int
    name: str
    image: str

class TVModel:
    def __init__(self):
        self.channels = [
            Channel(1, "News", "images/news.jpeg"),
            Channel(2, "Cartoons", "images/cartoons.jpeg"),
            Channel(3, "Football", "images/football.jpeg"),
            Channel(4, "Basketball", "images/basketball.jpeg"),
            Channel(5, "Golf", "images/golf.jpeg"),
            Channel(6, "College Basketball", "images/college_basketball.jpeg")
        ]
        self.current_index = 0
        self.is_on = False
        self.volume = 50
        self.prev_volume = 50
        self.is_muted = False

    def toggle_power(self):
        self.is_on = not self.is_on

    def channel_up(self):
        if self.is_on:
            self.current_index = (self.current_index + 1) % len(self.channels)

    def channel_down(self):
        if self.is_on:
            self.current_index = (self.current_index - 1) % len(self.channels)

    def set_channel(self, number):
        if self.is_on and 1 <= number <= len(self.channels):
            self.current_index = number - 1

    def volume_up(self):
        if self.is_on and self.volume < 100:
            self.is_muted = False
            self.volume = min(100, self.volume + 5)
            self.prev_volume = self.volume

    def volume_down(self):
        if self.is_on and self.volume > 0:
            self.is_muted = False
            self.volume = max(0, self.volume - 5)
            self.prev_volume = self.volume

    def toggle_mute(self):
        if self.is_on:
            if self.is_muted:
                self.is_muted = False
                self.volume = self.prev_volume
            else:
                self.is_muted = True
                self.prev_volume = self.volume
                self.volume = 0

    def get_current_channel(self):
        return self.channels[self.current_index]
