#classs with properties and default values :
#Part A - TV Base class 
class TV:
    #Constructor 
    def __init__(self, brand,on_off, price, inches):
        self.brand = brand
        self.channel = 1 #default value 
        self.volume = 50 #Default value 
        self.on_off = on_off
        self.price = price
        self.inches = inches
     #Increase volume method 
    def increase_volume(self):
        self.volume = min(self.volume + 1, 100) #Minimum volume cant be below Zero Maximum volume cant be above 100 
     #Decrease volume method 
    def decrease_volume(self):
        self.volume = max(self.volume - 1, 0) #Maximum volume cant be above 100 Minimum volume cant be below Zero
     #Set Channel methd 
    def set_channel(self, channel):
        self.channel = max(1, min(channel, 50))
     #Resetting the chanel and volume back to default value 
    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def get_status(self):
        return f"{self.brand} displaying channel {self.channel}, volume {self.volume}, {self.inches} inches, Price: ${self.price}, {'On' if self.on_off else 'Off'}"

# Usage of above created class and methods 
#Instance of the TV class , using a brand 
sony_tv = TV(brand="Sony", price=500, inches=42,on_off=True)

print(sony_tv.get_status())

sony_tv.increase_volume()
sony_tv.set_channel(8)

print(sony_tv.get_status())

sony_tv.reset_tv()
print(sony_tv.get_status())

