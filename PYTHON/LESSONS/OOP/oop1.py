# OOP of television remote control
class Television:
    def __init__(self, brand, size, resolution, power_status=False, volume=10, channel=1):
        self.brand = brand
        self.size = size
        self.resolution = resolution
        self.power_status = power_status
        self.volume = volume
        self.channel = channel
    def power_on(self):

        if not self.power_status:
            self.power_status = True
            print("The TV is now ON.")
        else:
            print("The TV is already ON.")

    def power_off(self):
        if self.power_status:
            self.power_status = False
            print("The TV is now OFF.")
        else:
            print("The TV is already OFF.")

    def change_channel(self, new_channel):
        if self.power_status:
            if 1 <= new_channel <= 100:
                self.channel = new_channel
                print(f"Channel changed to {self.channel}.")
            else:
                print("Invalid channel. Please select a channel between 1 and 100.")
        else:
            print("Please turn on the TV first.")

    def increase_volume(self):
        if self.power_status:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is at maximum level.")
        else:
            print("Please turn on the TV first.")

    def decrease_volume(self):
        if self.power_status:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is at minimum level.")
        else:
            print("Please turn on the TV first.")

    def __str__(self):
        power_state = "ON" if self.power_status else "OFF"
        return (f"Television({self.brand}, {self.size} inch, {self.resolution})\n"
                f"Power: {power_state}\n"
                f"Volume: {self.volume}\n"
                f"Channel: {self.channel}\n")

# Example usage:
tv = Television("Samsung", 55, "4K")
tv_1 = Television("Hisense", 43, "HD")
print(tv_1)

#tv.power_on()
#tv.increase_volume()
#tv.change_channel(10)
#tv.decrease_volume()
#tv.power_off()
#tv_1.power_on()
tv_1.decrease_volume()
tv_1.change_channel(2)
