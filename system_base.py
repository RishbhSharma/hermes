from component_base import Component

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

