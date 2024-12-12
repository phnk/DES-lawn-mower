from .event import Event

class CompleteEvent(Event):
    def __init__(self, id, current_state, eventqueue, complete_time, event_type="Complete Event"):
        super().__init__(current_state, eventqueue, complete_time, event_type)

        self.id = id

    def execute(self):

        self.get_state().add_time(self.get_time())
        SLA = self.get_state().get_SLA_list(self.id)
        released_mowers = SLA.complete_SLA()
        self.get_state().return_mowers(released_mowers)
        # TODO(carl): create new events?
