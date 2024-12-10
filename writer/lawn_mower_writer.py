from .writer import Writer

class LawnWriter(Writer):
    def __init__(self, state):
        super().__init__(state)

    def write(self):
        print(self.state.get_time())
