from dis import dis


class Dispatcher:
    def __init__(self):
        self.event_map = {}

    def register(self, event, op):
        op_list = self.event_map.get(event)
        if not op_list:
            self.event_map[event] = []
            op_list = self.event_map.get(event)
        op_list.append(op)

    def __str__(self):
        return str(self.event_map)


dispatcher = Dispatcher()
dispatcher.register("run", "runner")
dispatcher.register("jump", "jumper")
dispatcher.register("run", "walker")
print(dispatcher)
