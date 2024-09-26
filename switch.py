class Switch:
    def __init__(self):
        self.ID = ""
        self.number_of_ports = 0
        self._portStatus = []

    def boot(self):
        print(f"Switch {self.ID} is booting")

        self._portStatus = []
        for i in range(self.number_of_ports):
            self._portStatus.append(False)

    def connect(self, port):
        if port < 0 or port >= self.number_of_ports:
            print(f"Port {port} is not available in switch {self.ID}")
            return

        if self._portStatus[port]:
            print(f"Switch {self.ID} is already connected to port {port}")
            return

        self._portStatus[port] = True

        print(f"Switch {self.ID} is connecting to port {port}")

    def disconnect(self, port):
        if port < 0 or port >= self.number_of_ports:
            print(f"Port {port} is not available in switch {self.ID}")
            return
        
        if not self._portStatus[port]:
            print(f"Switch {self.ID} is already disconnected from port {port}")
            return
        
        self._portStatus[port] = False
        
        print(f"Switch {self.ID} is disconnecting from port {port}")


class ManagedSwitch(Switch):
    def __init__(self, IP):
        super().__init__()
        self.IP = IP

    def login(self):
        print(f"Managed switch {self.ID} is logging in")

    def set_ip(self, IP):
        if len(IP.split(".") ) != 4:
            print("falsch")

        octets = IP.split(".")
        for octet in octets:
            #todo check if octet is a number
            if int(octet) < 0 or int(octet) > 255:
                print("falsch")
                return
            
        self.IP = IP


mein_managed_switch = ManagedSwitch("10.16.1.1")
mein_managed_switch.ID = "MS-01"
mein_managed_switch.number_of_ports = 5

mein_managed_switch.boot()
mein_managed_switch.login()