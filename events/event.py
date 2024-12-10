class Event:
    def __init__(self, current_state, eventqueue, execution_time, event_name="abstract event"):
        self.current_state = current_state
        self.eventqueue = eventqueue
        self.execution_time = execution_time
        self.event_name = event_name

    def execute(self):
        pass

    def get_time(self):
        return self.execution_time

    def get_state(self):
        return self.current_state

    def get_queue(self):
        return self.eventqueue

    def get_event_name(self):
        return self.event_name
