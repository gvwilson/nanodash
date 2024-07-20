class Node:
    """Base class for DOM nodes."""

    # Indentation for pretty-printing
    SPACE = "  "

    class NodeIterator:
        """Iterate over children of node."""

        def __init__(self, target):
            self._target = target
            self._current = 0

        def __next__(self):
            assert isinstance(self._target, Node)
            if self._current >= len(self._target):
                raise StopIteration()
            child = self._target[self._current]
            self._current += 1
            return child

    def __init__(self, block, tag, *children):
        assert tag is not None
        self._block = block
        self._tag = tag
        self._children = children[:]

    @property
    def tag(self):
        return self._tag

    def __getitem__(self, i):
        assert -len(self._children) <= i < len(self._children)
        return self._children[i]

    def __len__(self):
        return len(self._children)

    def __iter__(self):
        return self.NodeIterator(self)

    def __str__(self):
        return self._pretty(0)

    def _pretty(self, depth):
        if len(self) == 0:
            return f"<{self.tag}></{self.tag}>"
        elif self._block:
            indent = self.SPACE * (depth + 1)
            temp = (f"{indent}{c if isinstance(c, str) else c._pretty(depth + 1)}" for c in self)
            return f"<{self.tag}>\n{'\n'.join(temp)}\n</{self.tag}>"
        else:
            temp = (c if isinstance(c, str) else str(c) for c in self)
            return f"<{self.tag}>{''.join(temp)}</{self.tag}>"


class Div(Node):
    def __init__(self, *children):
        super().__init__(True, "div", *children)

class Em(Node):
    def __init__(self, *children):
        super().__init__(False, "em", *children)

class Span(Node):
    def __init__(self, *children):
        super().__init__(False, "span", *children)
