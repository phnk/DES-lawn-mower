from .event import Event
from .sla_event import CreateSLAEvent
from .stop_event import StopEvent

class StartEvent(Event):
    def __init__(self, current_state, eventqueue):
        super().__init__(current_state, eventqueue, 0, "start event")

    def execute(self):
        state = self.get_state()
        queue = self.get_queue()

        # what do i do with the state here?
        create_time = self.get_state().get_time() + self.get_state().get_next_SLA_time()

        queue.add_event(CreateSLAEvent(state, queue, create_time))
        queue.add_event(StopEvent(state, queue, state.get_runtime()))

    def get_event_name(self):
        return "Start"
