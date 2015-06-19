# -*- coding: utf-8 -*-
from collections import deque


class BaseBinlogStreamReaderWrapper(object):
    """ This class is base class which implements peek/pop function, and subclass needs
    to implement _refill_current_events_if_empty and use self.current_events as a buffer.
    """

    def __init__(self):
        self.current_events = deque()

    def peek(self):
        """ Peek at the next event without actually taking it out of the stream.
        """
        self._refill_current_events_if_empty()
        return self.current_events[0]

    def pop(self):
        """ Takes the next event out from the stream, and return that event.
        Note that each data event contains exactly one row.
        """
        self._refill_current_events_if_empty()
        return self.current_events.popleft()

    def _refill_current_events_if_empty(self):
        raise NotImplementedError

    def _seek(self):
        raise NotImplementedError