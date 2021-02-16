import sqlite3 as sl
import platform
import subprocess
from time import time

database_file = 'firstdb.db'

'''
=============
PING FUNCTION
=============
'''
def ping(host):

    param = '-n' if platform.system().lower()== 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


class Database:
    def __init__(self, file):
        self.db = self.getConnection(file)
        self.file = file

    def queryToDict(self, sql):
        cursor = self.db.execute(sql)
        description = cursor.description
        columns = [col[0] for col in description]
        data = [ dict(zip(columns, row)) for row in cursor.fetchall() ]
        return data

    def getConnection(self, db):
        connection = sl.connect(db)
        return connection

    def getSystemById(self, sys_id):
        sql = "SELECT * FROM SYSTEMS WHERE ID = " + str(sys_id)
        return self.queryToDict(sql)[0]

    def getAllSystems(self):
        sql = "SELECT * FROM SYSTEMS"
        return self.queryToDict(sql)


class Component:
    config = {  'status_time' : None ,
                'status' : 'offline',
            }
    def __init__(self, name):
        self.name = name

    def update_status(self, online = False):
        if online:
            self.config['status'] = 'online'
        else:
            self.config['status'] = 'offline'

        self.config['status_time'] = time()


class System(Component):

    config = {'type':'private',
              'ping_fx': ping }

    priorities = {'private': 2,
                  'public': 1}

    def __init__(self, sys_id, sys_ip):
        self.id = sys_id
        self.host_ip = sys_ip
        self.ping_fx = System.config['ping_fx']

        self.component = Component('interface')

    def ping(self):
        if self.ping_fx != None:
            # use a return code ???
            online = self.ping_fx( self.host_ip )
            self.update_status(online)

class Network:

    config = { 'dummy_param' : True }

    def __sizeof__(self):
        return len(self.systems_ip)

    def __init__(self, id):
        self.id = id

        # sys_id, ip
        self.systems_ip = {}

        # sys_id, System_obj
        self.systems_component = {}

    def add_system(self, id, host_ip):
        self.systems_ip[id] = host_ip
        self.systems_component[id] = System(id, host_ip)

        return (id in self.systems_ip)

    def report(self):
        return [ s.ping() for _ , s in self.systems_component ]

    def get_system_by_id(self, id):
        return self.systems_component[id]