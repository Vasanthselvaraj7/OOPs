#Multiple Inheritance
"""
#base class

class Document:
    def __init__(self,Title, Author):
        self.Title = Title
        self.Author = Author

    def Dispaly_info(self):
        return f"Title : {self.Title}, Author : {self.Author}"

#Derived Class1
class Printable(Document):

    def Print_Document(self):
        return f"Printing {self.Title} by {self.Author}"

#Derived Class 2
class Scannable(Document):
    def Scan_Document(self, year):
        self.year = year
        return f"Scanning {self.Title} by {self.Author}, year {self.year}"

#
class PrintAndScan(Printable, Scannable):
    def Display_info(self):
        return f"Title: {self.Title} by Author: {self.Author} Printing, Scanning"


Document = Document("Vampire Diaries", "L.J.Smith")
Printable = Printable("The Originals", "Julie Plec")
Scannable = Scannable("Transformers", "Michale Bay")
PAS = PrintAndScan("Harry Potter", "J.K.Rolling")

print(Document.Dispaly_info())
print(Printable.Print_Document())
print(Scannable.Scan_Document())
print(PAS.Display_info())
"""

#Base Class
"""
class Power_Device:

    def power_on(self):
        print("Device is power ON")

    def power_of(self):
        print("Device is power OFF")

class Music_player:
    def play_music(self):
        print("Playing Music")

    def stop_music(self):
        print("Music stopped")

class Camera():
    def take_picture(self):
        print("Picture Taken")

#Derived Class

class Smart_Phone(Power_Device, Music_player, Camera):
    def details(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display(self):
        return f"The Smart Phone Name : {self.name}, Model : {self.model}, Year : {self.year}"

mobile = Smart_Phone()
mobile.details("Motorola", "G34", 2024)
print(mobile.display())
mobile.power_on()
mobile.take_picture()
mobile.play_music()
mobile.stop_music()
mobile.power_of()
"""
#using method_overriding and super()
"""
class Device:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def status(self):
        print(f"Status of{self.name} : OK")

class PowerDevice(Device):
    def __init__(self, id, name, power_status=False):
        super().__init__(id, name)
        self.power_status = power_status
    def power_on(self):
        print(self.name,"is powered ON")

    def power_off(self):
        print(self.name, "is powered OFF")

class NetworkDevice(Device):
    def __init__(self, id, name, ip_address):
        super().__init__(id, name)
        self.ip_address = ip_address

    def connect(self):
        print(f"{self.name} connect to network with ip{self.ip_address}")

    def disconnect(self):
        print(f"{self.name} Disconnect from network")

#derived class

class Smart_Light(PowerDevice, NetworkDevice):
    def __init__(self, id, name, ip_address, power_status=False, brightness=0):
        PowerDevice.__init__(self, id, name, power_status)
        NetworkDevice.__init__(self, id, name, ip_address)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} brightness set to {level}")

    def status(self):
        print(f"Status of{self.name}, Level is {self.brightness} : OK")

smartlight = Smart_Light(101, "Moto", "123456.789.0")
smartlight.status()
smartlight.power_on()
smartlight.connect()
smartlight.set_brightness(75)
smartlight.status()
smartlight.disconnect()
smartlight.power_off()
"""


class Device:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name

    def status(self):
        print(f"Status of {self.name}: OK")


class PowerDevice(Device):
    def __init__(self, device_id, name, power_status=False):
        super().__init__(device_id, name)
        self.power_status = power_status

    def power_on(self):
        self.power_status = True
        print(f"{self.name} is powered ON")

    def power_off(self):
        self.power_status = False
        print(f"{self.name} is powered OFF")


class NetworkDevice(Device):
    def __init__(self, device_id, name, ip_address):
        super().__init__(device_id, name)
        self.ip_address = ip_address

    def connect(self):
        print(f"{self.name} connected to network with IP {self.ip_address}")

    def disconnect(self):
        print(f"{self.name} disconnected from network")


class SmartLight(PowerDevice, NetworkDevice):
    def __init__(self, device_id, name, ip_address, power_status=False, brightness=0):
        PowerDevice.__init__(self, device_id, name, power_status)
        NetworkDevice.__init__(self, device_id, name, ip_address)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} brightness set to {level}")

    def status(self):
        super().status()
        print(f"{self.name} brightness level is {self.brightness}")


# Testing the SmartLight class
smart_light = SmartLight(device_id=1, name="Living Room Light", ip_address="192.168.1.10")
smart_light.status()
smart_light.power_on()
smart_light.connect()
smart_light.set_brightness(75)
smart_light.status()
smart_light.power_off()
smart_light.disconnect()

