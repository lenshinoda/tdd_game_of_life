

class Cell:
    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if not state in [0, 1]:
            raise Exception("Invalid state")
        self._state = state