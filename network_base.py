from system_base import System

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