from .event import Event

class StopEvent(Event):
    def __init__(self, current_state, eventqueue, runtime):
        super().__init__(current_state, eventqueue, runtime, "stop event")

    def execute(self):
        state = self.get_state()

        # what do i do with the state here?
        state.stop_sim()

    def get_event_name(self):
        return "Stop"
