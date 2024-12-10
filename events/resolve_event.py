from .event import Event
from .complete_event import CompleteEvent

class ResolveViolationEvent(Event):
    def __init__(self, id, current_state, eventqueue, fixing_time, event_type="Fix Violation Event"):
        super().__init__(current_state, eventqueue, fixing_time, event_type)

        self.id = id

    def execute(self):
        SLA = self.get_state().get_SLA(self.id)

        SLA.set_status("ON_GOING")

        # TODO(carl): generate chance of violation else complete event
