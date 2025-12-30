
class Phone:
    def call(self):
        print("Calling from phone")

class Camera:
    def click(self):
        print("Taking photo")

class Smartphone(Phone, Camera):
    def browse(self):
        print("Browsing internet")

s = Smartphone()
s.call()
s.click()
s.browse()
