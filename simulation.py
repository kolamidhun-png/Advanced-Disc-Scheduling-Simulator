# disk_scheduler.py
import math
import matplotlib.pyplot as plt
from collections import deque

class DiskScheduler:
    def __init__(self, requests, head, disk_size=None):
        """
        requests: list of integer track numbers (0..disk_size-1 if disk_size provided)
        head: starting head position (int)
        disk_size: optional maximum number of tracks (int)
        """
        self.requests = list(requests)
        self.head = int(head)
        self.disk_size = disk_size

    def _metrics(self, order):
        """Return total movement, avg movement, and per-step movements"""
        pos = self.head
        movements = []
        for p in order:
            movements.append(abs(p - pos))
            pos = p
        total = sum(movements)
        avg = total / len(movements) if movements else 0
        return total, avg, movements

    def fcfs(self):
        order = list(self.requests)
        return order, *self._metrics(order)

    def sstf(self):
        pending = set(self.requests)
        pos = self.head
        order = []
        while pending:
            closest = min(pending, key=lambda x: abs(x - pos))
            order.append(closest)
            pending.remove(closest)
            pos = closest
        return order, *self._metrics(order)

    def scan(self, direction='up'):
        """
        SCAN goes to the end of disk (0 or disk_size-1) before reversing.
        disk_size required for full SCAN; if not provided, assume min/max of requests as ends.
        """
        if not self.requests:
            return [], 0, 0, []
        size = self.disk_size
        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])
        order = []
        if direction == 'up':
            order += right
            if size is not None:
                order.append(size - 1)  # go to disk end
            order += list(reversed(left))
        else:
            order += list(reversed(left))
            if size is not None:
                order.append(0)
            order += right
        return order, *self._metrics(order)

    def cscan(self, direction='up'):
        """
        Circular SCAN: when head reaches end it jumps to start without servicing in between.
        For simulation we treat the jump as movement equal to abs(end-start) if disk_size provided.
        """
        if not self.requests:
            return [], 0, 0, []
        size = self.disk_size
        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])
        order = []
        if direction == 'up':
            order += right
            if size is not None:
                order.append(size - 1)  # sweep to end
                order.append(0)         # jump to start
            order += left
        else:
            order += list(reversed(left))
            if size is not None:
                order.append(0)
                order.append(size - 1)
            order += right
        return order, *self._metrics(order)

    def look(self, direction='up'):
        """
        LOOK: like SCAN but reverse at the last request instead of going to disk end.
        """
        if not self.requests:
            return [], 0, 0, []
        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])
        order = []
        if direction == 'up':
            order += right
            order += list(reversed(left))
        else:
            order += list(reversed(left))
            order += right
        return order, *self._metrics(order)

    def clook(self, direction='up'):
        """
        C-LOOK: like C-SCAN but only jump between last and first request (no travel to disk ends)
        """
        if not self.requests:
            return [], 0, 0, []
        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])
        order = []
        if direction == 'up':
            order += right
            if left:
                # jump to smallest left and continue ascending
                order += left
        else:
            order += list(reversed(left))
            if right:
                order += list(reversed(right))
        return order, *self._metrics(order)

    def simulate_all(self, visualize=True, direction='up'):
        results = {}
        results['FCFS'] = self.fcfs()
        results['SSTF'] = self.sstf()
        results['SCAN'] = self.scan(direction=direction)
        results['C-SCAN'] = self.cscan(direction=direction)
        results['LOOK'] = self.look(direction=direction)
        results['C-LOOK'] = self.clook(direction=direction)
        if visualize:
            self._plot(results)
        return results

    def _plot(self, results):
        # For each algorithm, plot head positions over sequence number
        n_plots = len(results)
        fig, axes = plt.subplots(n_plots, 1, figsize=(8, 2.2 * n_plots), sharex=False)
        if n_plots == 1:
            axes = [axes]
        for ax, (alg, (order, total, avg, moves)) in zip(axes, results.items()):
            # Build positions (start then each serviced position)
            pos = [self.head] + list(order)
            ax.step(range(len(pos)), pos, where='post')
            ax.scatter(range(len(pos)), pos, s=10)
            ax.set_ylabel('Track')
            ax.set_title(f"{alg} — total movement={total}, avg={avg:.2f}")
            ax.grid(True, linestyle=':', linewidth=0.5)
        axes[-1].set_xlabel('Sequence step (0=start)')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # sample request set
    requests = [95, 180, 34, 119, 10, 100, 62, 198]
    head = 80
    disk_size = 200   # optional

    sim = DiskScheduler(requests=requests, head=head, disk_size=disk_size)
    results = sim.simulate_all(visualize=True, direction='up')

    # Print summarized results
    for alg, (order, total, avg, moves) in results.items():
        print(f"\n{alg}:")
        print(" Service order:", order)
        print(" Total head movement:", total)
        print(" Average per request:", round(avg, 2))
        print(" Per-step movements:", moves)
