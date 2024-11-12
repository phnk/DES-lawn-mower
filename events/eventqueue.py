class EventQueue:
    def __init__(self):
        self.eventqueue = []

    def add_event(self, incoming_event):
        if len(self.eventqueue) < 0:
            raise Exception("Got negative length for the eventqueue")
        elif len(self.eventqueue) == 0:
            self.eventqueue.append(incoming_event)
        # event has to have a time that we can sort off
        else:
            for i, current_event in enumerate(self.eventqueue):
                if incoming_event.get_time() <= current_event.get_time():
                    self.eventqueue.insert(i, incoming_event)
                    break

    def run_event(self):
        if len(self.eventqueue) == 0:
            raise Exception("Got no length in run_event")
        current_event = self.eventqueue.pop(0)
        current_event.execute()


    def clear_queue(self):
        self.eventqueue = []

    def has_next(self):
        return len(self.eventqueue) != 0

