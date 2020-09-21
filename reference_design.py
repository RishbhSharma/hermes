from random import randint

#class DS:
#    def __init__(self, data1, data2):
#        self.d1=data1
#        self.d2=data2

class System():
    def __init__(self, sys_id):
        self.id = sys_id
        self.online = self.ping()
        print( "System Initialized. ID = ", sys_id )

        # unused
        self.iface = "interface"

    def ping(self):
        return randint(0,1)

    def register(self):
        print("System registred on", self.iface)

#class Network:
#    def __init__(self, sys_ids):

if __name__ == "__main__":ssss
    a = System(1)
    b = System(5)
    print(a.ping(),b.ping())