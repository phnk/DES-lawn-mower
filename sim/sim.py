class Sim():
    def __init__(self, state, queue, writer, start_event, stop_event):
        self.state = state
        self.queue = queue
        self.writer = writer

        self.queue.add_event(start_event)
        self.queue.add_event(stop_event)

    def run(self):
        while (self.queue.has_next() and self.state.is_running() == True):
            self.queue.run_event()
            self.writer.write()
