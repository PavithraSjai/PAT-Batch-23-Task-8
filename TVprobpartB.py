#Base Class TV
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1 #default value
        self.volume = 50 #default value
        self.on = False # Tv is off by default 
        self.price = price
        self.inches = inches
    #volume increase & decrease methods 
    def increase_volume(self):
        self.volume = min(self.volume + 1, 100)

    def decrease_volume(self):
        self.volume = max(self.volume - 1, 0)
    #Channel set and Reset of channel and volume 
    def set_channel(self, channel):
        self.channel = max(1, min(channel, 50))

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    #Getting TV status method 
    def get_status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}, {self.inches} inches, Price: ${self.price}, {'On' if self.on else 'Off'}"

#Child class LED 
class LEDTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches) #inheriting the brand , price and inches from base class TV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"{self.brand} LED TV - Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, Refresh Rate: {self.refresh_rate} Hz"

#Child class Plasma
class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, price, inches) #inheriting the brand , price and inches from base class TV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return f"{self.brand} Plasma TV - Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"


# Example Usage
led_tv = LEDTV("Samsung", 800, 55, "Slim", "Low", 5, 120)
plasma_tv = PlasmaTV("Sony", 1000, 60, "Thick", "High", 8, 60, "Wide", "LED")

print(led_tv.display_details())
print(plasma_tv.display_details())

# Common TV methods inherited under child class 
led_tv.increase_volume()
led_tv.set_channel(22)
plasma_tv.set_channel(15)

print(led_tv.get_status())
print(plasma_tv.get_status())
