class EventSystem(object):

    def __init__(self):
        self.eventListeners = {}

    def on(self, event, func):
        if event in self.eventListeners:
            self.eventListeners[event].append(func)
        else:
            self.eventListeners[event] = [func]

    def trigger(self, event):
        if event in self.eventListeners:
            for fn in self.eventListeners[event]:
                fn()
