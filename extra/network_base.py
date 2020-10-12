#from system_base import System
from time import time,sleep
from random import randint
from extra.variables import sys_debug,delay_ms

def wait(): sleep(delay_ms/1000.0)
def wait_r(): sleep(delay_ms/1000.0*randint(1,10))

class Component:
    def __init__(self, comp_name, comp_data = None):
        self.name = comp_name
        self.last_seen = time()
        self.is_on = False
        self.is_online = False
        self.data = comp_data
        #print("Initializing component", comp_name)
        #print("")
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

        #if self.app():
        #    self.system.came_online()

        self.register()
        print( "System Initialized ( ID = ", sys_id, "; debug =", self.debug, ")" )

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
            self.reg_id = int((t-int(t))*1000)
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
        return [ s.ping() for s in self.nws ]

    def check(self):
        print("Performing check. Number of systems_ip =",self.size)

        report = self.report()
        print("Check complete")

        #for id, stat in zip(self.networks, report):
        #    print(id,stat)

        online = sum(report)
        offline = self.size - online
        print(online, offline, "System(s) online/offline")
