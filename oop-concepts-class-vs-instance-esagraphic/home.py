class TV:
    def __init__(self):
        self.channel = 1  # Channel starts at 1
        self.volume_level = 1  # Volume starts at 1
        self.turned_on = False  # TV is off by default

    def turn_on(self):
        self.turned_on = True
        print('The TV is on now')

    def turn_off(self):
        self.turned_on = False
        print('The TV is off now')

    def channel_up(self):
        if self.turned_on:
            if self.channel < 100:  # Check if channel is less than 100
                self.channel += 1
                print(f'The channel is now {self.channel}')
            else:
                print('Channel cannot go higher than 100')
        else:
            print('TV is off, cannot change channel')

    def channel_down(self):
        if self.turned_on:
            if self.channel > 1:  # Check if channel is greater than 1
                self.channel -= 1
                print(f'The channel is now {self.channel}')
            else:
                print('Channel cannot go lower than 1')
        else:
            print('TV is off, cannot change channel')

    def set_channel(self, channel_number):
        if self.turned_on:
            if 1 <= channel_number <= 100:  # Check if the channel is between 1 and 100
                self.channel = channel_number
                print(f'The channel is now {self.channel}')
            else:
                print('The channel must be between 1 and 100')
        else:
            print("TV is off, cannot change channel")

    def volume_up(self):
        if self.turned_on:
            if self.volume_level < 10:  # Volume range is 1 to 10
                self.volume_level += 1
                print(f'The volume is now {self.volume_level}')
            else:
                print('Volume cannot go higher than 10')
        else:
            print('TV is off, cannot change volume')

    def volume_down(self):
        if self.turned_on:
            if self.volume_level > 1:  # Volume cannot go lower than 1
                self.volume_level -= 1
                print(f'The volume is now {self.volume_level}')
            else:
                print('Volume cannot go lower than 1')
        else:
            print('TV is off, cannot change volume')

    def set_volume(self, volume_number):
        if self.turned_on:
            if 1 <= volume_number <= 10:  # Volume range is 1 to 10
                self.volume_level = volume_number
                print(f'The volume is now {self.volume_level}')
            else:
                print('The volume must be between 1 and 10')
        else:
            print("TV is off, cannot change volume")
