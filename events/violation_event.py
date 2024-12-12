from .event import Event
from .resolve_event import ResolveViolationEvent

class ViolationEvent(Event):
    def __init__(self, id, current_state, eventqueue, violation_time, event_type="Violation Event"):
        super().__init__(current_state, eventqueue, violation_time, event_type)

        self.id = id

    def execute(self):
        SLA = self.get_state().get_SLA(self.id)

        SLA.set_status("VIOLATION")
        self.get_state().add_time(self.get_time())

        # Resolve time
        resolve_time = self.get_state().get_time() * self.get_state().get_violation_time()
        self.get_queue().add_event(ResolveViolationEvent(id, self.get_state(), self.get_queue(), resolve_time))
