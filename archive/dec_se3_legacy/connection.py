import numpy as np
from .se3 import compose, inverse, identity

class SE3Connection:
    def __init__(self, transports):
        self._g = {}
        for (u, v), A in transports.items():
            self._g[(u, v)] = A
            self._g[(v, u)] = inverse(A)

    def transport(self, u, v):
        return self._g[(u, v)]

    def path_transport(self, path):
        A = identity()
        for u, v in zip(path[:-1], path[1:]):
            A = compose(self.transport(u, v), A)
        return A

    def loop_transport(self, loop):
        assert loop[0] == loop[-1]
        return self.path_transport(loop)
