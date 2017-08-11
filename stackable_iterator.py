"""stackable_iterator module."""


class Stackerator(object):
    """
    Iterator that supports push operations, like a stack.

    The last element to be pushed to the iterator is the next element out.
    """

    def __init__(self, it):
        """Instantiate object."""
        self.it = it
        # See if there are any elements
        try:
            first = it.next()
        except StopIteration:
            self._exhausted = True
        else:
            self._exhausted = False
            self.push(first)

    @property
    def pushed(self):
        """Return elements pushed to this StackableIterator."""
        if not hasattr(self, '_pushed'):
            self._pushed = []
        return self._pushed

    @property
    def exhausted(self):
        """Return True if there aren't any more elements in this iterator."""
        if not self.pushed and self._exhausted:
            return True
        else:
            try:
                next_val = next(self)
            except StopIteration:
                return True
            else:
                self.push(next_val)
                return False

    def __iter__(self):
        """Return self."""
        return self

    def next(self):
        """Return the next element."""
        if self.pushed:
            return self.pushed.pop()
        else:
            try:
                return self.it.next()
            except StopIteration:
                self._exhausted = True
                raise StopIteration

    def push(self, val):
        """Add an element to the front of the iterator."""
        self.pushed.append(val)
