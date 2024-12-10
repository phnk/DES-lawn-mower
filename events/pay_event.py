from .event import Event
from .violation_event import ViolationEvent
from .complete_event import CompleteEvent

class PayEvent(Event):
    def __init__(self, id, current_state, eventqueue, pay_event_time, event_type="Pay Event"):
        super().__init__(current_state, eventqueue, pay_event_time, event_type)

        # ASSUMPTION: id is the same as index in our SLA array in the state
        self.id = id

    def execute(self):
        # do we want to have a fail here and make a new pay event?
        SLA = self.get_state().get_SLA_list(self.id)
        SLA.change_payment_status("PAYMENT_COMPLETE")

        # TODO(carl): need to take the number of mowers
        self.get_state().take_mowers(SLA.number_of_lawn_mowers())

        # TODO(carl): add a chance for the payment to fail and decide what to do with the SLA. Drop?
        if self.get_state().get_violation_rng():
            # make violation event by getting time
            # remember id
            violation_time = self.get_state().get_time() * self.get_state().get_violation_time()
            self.get_queue().add_event(ViolationEvent(self.id, self.get_state(), self.get_queue(), violation_time))
        else:
            # generate complete event?
            SLA.set_status("ON_GOING")
            complete_time = self.get_state().get_time() * self.get_state().get_complete_time()
            self.get_queue().add_event(CompleteEvent(self.id, self.get_state(), self.get_queue(), complete_time))
