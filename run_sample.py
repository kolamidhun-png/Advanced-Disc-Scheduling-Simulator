from disk_scheduler import DiskScheduler
from disk_scheduler.plotter import plot_results


if __name__ == '__main__':
requests = [95, 180, 34, 119, 10, 100, 62, 198]
head = 80
disk_size = 200


sim = DiskScheduler(requests=requests, head=head, disk_size=disk_size)
results = sim.simulate_all(visualize=False, direction='up')


# Print summaries
for alg, (order, total, avg, moves) in results.items():
print(f"\n{alg}:")
print(" Service order:", order)
print(" Total head movement:", total)
print(" Average per request:", round(avg, 2))
print(" Per-step movements:", moves)


# Visualize
plot_results(head, results)
