from extra.ping import ping
sys_debug = True


class System:
    def __init__(self, sys_ip, sys_mac, sys_debug=sys_debug):
        self.is_online = False

        self.mac_addr = sys_mac
        self.ip_addr = sys_ip
        self.debug = sys_debug

        print("System Initialized ( ID = ", sys_ip, "; debug = ", self.debug, ")")

    def ping(self):
        if self.debug:
            return ping(self.ip_addr)
        else:
            return 1

class Network:
    def __init__(self, sys_ids = None):
        self.system_ids = sys_ids
        self.systems = dict()

        if sys_ids is not None:
            self.size = len(sys_ids)
            for id in sys_ids:
                self.systems[id] = System
        else:
            self.size = 0

    def add_system(self):
        return True

    def report(self):
        return [ self.systems[s].ping() for s in self.system_ids ]
