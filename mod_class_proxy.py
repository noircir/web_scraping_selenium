class Proxy:
    def __init__(self, ip, port, location, speed, type_, anonymity, last):
        self.ip = ip
        self.port = port
        self.location = location
        self.speed = speed
        self.type_ = type_
        self.anonymity = anonymity
        self.last = last

    def __str__(self):
        return 'IP: {} Port: {} Location: {} Speed: {} Type: {} Anonymity: {} Last: {}'.\
            format(self.ip, self.port, self.location, self.speed, self.type_, self.anonymity, self.last)