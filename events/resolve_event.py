from .event import Event
from .complete_event import CompleteEvent

class ResolveViolationEvent(Event):
    def __init__(self, id, current_state, eventqueue, fixing_time, event_type="Fix Violation Event"):
        super().__init__(current_state, eventqueue, fixing_time, event_type)

        self.id = id

    def execute(self):
        SLA = self.get_state().get_SLA(self.id)

        SLA.set_status("ON_GOING")
        self.get_state().add_time(self.get_time())

        # TODO(carl): add a chance for the payment to fail and decide what to do with the SLA. Drop?
        # generate complete event?
        complete_time = self.get_state().get_time() * self.get_state().get_complete_time()
        self.get_queue().add_event(CompleteEvent(self.id, self.get_state(), self.get_queue(), complete_time))

