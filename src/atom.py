from interface import Eval


class Symbol(Eval):
    def __init__(self, n):
        self.name = n

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def eval(self, env, args=None):
        return env.get(self.name)
