class WLAN:
    def __init__(self, sta_if):
        self.status_value = 0
    def active(self, state=None):
        return True
    def connect(self, ssid, password):
        pass
    def status(self):
        if self.status_value < 3:
            self.status_value = self.status_value + 1
        return self.status_value
    def ifconfig(self):
        return ['ip address']
    def config(self, essid, password):
        pass

class STA_IF:
    pass
class AP_IF:
    pass