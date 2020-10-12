class Component:
    def __init__(self):
        self.last_seen = time()
        self.is_online = False

    def came_online(self):
        self.is_online = True
        self.last_seen = time()

    def went_offline(self, reason=None):
        self.is_online = False

    def get_status(self):
        return self.is_online, self.last_seen


class System(Component):

    config = {'type':'private',
              'ping_fx': None}

    priorities = {'private': 2,
                  'public: 1'}

    def __init__(self, sys_id):
        self.id = sys_id
        self.reg_time = None
        self.ping_fx = System.config['ping_fx']

        self.system = Component('interface')
        #self.start()

    def ping(self):
        if self.ping_fx != None:
            return self.ping_fx()

class Network:
    def __init__(self, sys_ids):
        self.networks = sys_ids
        self.size = len(sys_ids)
        self.nws = [ System(id) for id in sys_ids ]

    def report(self):
        return [ s.ping() for s in self.nws ]

    def check(self):
        print("Performing check. Number of systems_ip =",self.size)

        report = self.report()
        print("Check complete")

        online = sum(report)
        offline = self.size - online
        print(online, offline, "System(s) online/offline")

