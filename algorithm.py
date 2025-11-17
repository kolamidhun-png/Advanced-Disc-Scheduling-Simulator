"""Core disk scheduling implementations.
if not self.requests:
return self._metrics([])
size = self.disk_size
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order.extend(right)
if size is not None:
# sweep to end, then jump to start (we include end and start as traversal points)
order.append(size - 1)
order.append(0)
order.extend(left)
else:
order.extend(reversed(left))
if size is not None:
order.append(0)
order.append(size - 1)
order.extend(right)
return self._metrics(order)


def look(self, direction: str = "up"):
if not self.requests:
return self._metrics([])
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order.extend(right)
order.extend(reversed(left))
else:
order.extend(reversed(left))
order.extend(right)
return self._metrics(order)


def clook(self, direction: str = "up"):
if not self.requests:
return self._metrics([])
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order.extend(right)
if left:
# jump directly to the smallest left request
order.extend(left)
else:
order.extend(reversed(left))
if right:
order.extend(reversed(right))
return self._metrics(order)
