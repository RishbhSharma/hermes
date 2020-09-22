from random import randint
from time import time,sleep

#class DS:
#    def __init__(self, data1, data2):
#        self.d1=data1
#        self.d2=data2

delay_ms = 100
sys_debug = True

def wait(): sleep(delay_ms/1000.0)
def wait_r(): sleep(delay_ms/1000.0*randint(1,10))

'''
class Status:
    def __init__(self):
        self.last_seen = time()
        self.is_online = False
    
    def came_online(self):
        self.is_online = True
        self.last_seen = time()
        
    def went_offline(self, reason = None):
        self.is_online = False
        
    def get_status(self):
        return self.is_online, self.last_seen
    
#class Ping:
#    def __init__(self, ip_addr):
#        self.ip = ip_addr
'''
class Component:
    def __init__(self, comp_name, comp_data = None):
        self.name = comp_name
        self.last_seen = time()
        self.is_on = False
        self.is_online = False
        self.data = comp_data
        print("Initializing component", comp_name)
        wait()

    def came_online(self):
        if self.is_on == False:
            self.is_on = True
        self.is_online = True
        self.last_seen = time()

    def went_offline(self, reason=None):
        self.is_online = False

    def get_status(self):
        return self.is_online, self.last_seen




class System(Component):
    def __init__(self, sys_id):
        self.id = sys_id
        self.debug = sys_debug
        self.reg_id = None

        if self.debug:
            self.system = Component("debug_iface")
        else:
            self.system = Component("running_iface")

        if self.ping():
            self.system.came_online()
        print( "System Initialized. ID = ", sys_id, "debugging =", self.debug )

        # unused
        #self.iface = "interface"

    def ping(self):
        if self.debug:
            wait_r()
            return randint(0,1)
        else:
            return 1

    def register(self):
        if self.reg_id == None:
            on = self.ping()
            t = time()
            self.reg_id = t
            if on:
                self.system.came_online()

            print("System", self.system.name)
            print("registered at time", t)
            print("Status:",on)


class Network:
    def __init__(self, sys_ids):
        self.networks = sys_ids
        self.size = len(sys_ids)
        self.nws = [System(id) for id in sys_ids]

    def report(self):
        return [s.ping() for s in self.nws]

    def check(self):
        print("Performing check. Number of systems =",self.size)

        report = self.report()
        print("Check complete")
        for id, stat in zip(self.networks, report):
            print(id,stat)

        online = sum(report)
        offline = self.size - online
        print(online, offline, "System(s) online/offline")


if __name__ == "__main__":
    #a = System(1)
    #b = System(5)
    #print(a.ping(),b.ping())

    n = Network([6,7,5,3,9])
    n.check()
