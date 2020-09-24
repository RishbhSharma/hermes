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