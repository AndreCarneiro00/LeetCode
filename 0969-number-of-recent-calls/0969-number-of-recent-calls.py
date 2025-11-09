from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.queue = deque([])

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        tail = self.queue[-1]
        head = self.queue[0]
        while tail - head > 3000 and self.queue:
            self.queue.popleft()
            tail = self.queue[-1]
            head = self.queue[0]

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)