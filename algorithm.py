import math
return self._metrics(order)


def cscan(self, direction: str = "up"):
if not self.requests:
return self._metrics([])
size = self.disk_size
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order += right
if size is not None:
order.append(size - 1)
order.append(0)
order += left
else:
order += list(reversed(left))
if size is not None:
order.append(0)
order.append(size - 1)
order += right
return self._metrics(order)


def look(self, direction: str = "up"):
if not self.requests:
return self._metrics([])
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order += right
order += list(reversed(left))
else:
order += list(reversed(left))
order += right
return self._metrics(order)


def clook(self, direction: str = "up"):
if not self.requests:
return self._metrics([])
left = sorted([r for r in self.requests if r < self.head])
right = sorted([r for r in self.requests if r >= self.head])
order = []
if direction == "up":
order += right
if left:
order += left
else:
order += list(reversed(left))
if right:
order += list(reversed(right))
return self._metrics(order)


def simulate_all(self, visualize: bool = True, direction: str = "up"):
results = {}
results["FCFS"] = self.fcfs()
results["SSTF"] = self.sstf()
results["SCAN"] = self.scan(direction=direction)
results["C-SCAN"] = self.cscan(direction=direction)
results["LOOK"] = self.look(direction=direction)
results["C-LOOK"] = self.clook(direction=direction)
return results
