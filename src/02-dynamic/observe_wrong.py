"""Observer/observable."""

import sys


class Active:
    def __init__(self, name):
        self._name = name
        self._observers = []

    def observe(self, *others):
        for o in others:
            if self not in o._observers:
                o._observers.append(self)

    def notify(self, message, origin=None):
        assert (origin is None) or (origin is not self), "Circular"
        self.action(message)
        if origin is None:
            origin = self
        for other in self._observers:
            other.notify(message, origin)

    def action(self, message):
        print(f"- {self._name} gets {message}")

    def __str__(self):
        return f"{self._name}:({','.join(o._name for o in self._observers)})"


def test_simple():
    print("simple test")
    a = Active("a")
    b = Active("b")
    a.observe(b)
    b.notify("trying")


def test_circular():
    print("circular test")
    a = Active("a")
    b = Active("b")
    a.observe(b)
    b.observe(a)
    try:
        b.notify("trying")
        print("this should not have worked")
    except AssertionError:
        print("got circularity exception as expected")


def test_multi():
    print("multi test")
    a = Active("a")
    b = Active("b")
    c = Active("c")
    a.observe(b, c)
    b.observe(c)
    c.notify("trying")


if __name__ == "__main__":
    func = globals()[f"test_{sys.argv[1]}"]
    func()
