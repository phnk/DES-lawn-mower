from .event import Event
from .pay_event import PayEvent

class CreateSLAEvent(Event):
    def __init__(self, current_state, eventqueue, create_time):
        super().__init__(current_state, eventqueue, create_time, "SLA event")

    def execute(self):
        # create SLA
        id = self.get_state().get_SLA()

        self.get_state().add_time(self.get_time())
        # random violation event

        # create pay event with some random
        pay_event_time = self.get_state().get_time() * self.get_state().get_pay_time()
        self.get_queue().add_event(PayEvent(id, self.get_state(), self.get_queue(), pay_event_time, "Pay event"))
