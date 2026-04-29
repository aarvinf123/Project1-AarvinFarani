class TVController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        view.power_btn.clicked.connect(self.power)
        view.channel_up_btn.clicked.connect(self.channel_up)
        view.channel_down_btn.clicked.connect(self.channel_down)
        view.volume_up_btn.clicked.connect(self.volume_up)
        view.volume_down_btn.clicked.connect(self.volume_down)
        view.mute_btn.clicked.connect(self.mute)

        for i, btn in enumerate(view.num_buttons, 1):
            btn.clicked.connect(lambda checked, n=i: self.set_channel(n))

        self.update_view()

    def power(self):
        self.model.toggle_power()
        self.update_view()

    def channel_up(self):
        self.model.channel_up()
        self.update_view()

    def channel_down(self):
        self.model.channel_down()
        self.update_view()

    def volume_up(self):
        self.model.volume_up()
        self.update_view()

    def volume_down(self):
        self.model.volume_down()
        self.update_view()

    def mute(self):
        self.model.toggle_mute()
        self.update_view()

    def set_channel(self, number):
        self.model.set_channel(number)
        self.update_view()

    def update_view(self):
        if not self.model.is_on:
            self.view.show_off()
            self.view.volume_bar.setValue(0)
            self.view.volume_bar.setEnabled(False)
            return

        channel = self.model.get_current_channel()
        self.view.show_channel(channel.image)
        self.view.volume_bar.setValue(self.model.volume)
        self.view.volume_bar.setEnabled(not self.model.is_muted)
