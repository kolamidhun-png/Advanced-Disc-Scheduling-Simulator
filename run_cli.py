import argparse
from disk_scheduler import DiskScheduler
from disk_scheduler.plotter import plot_results


parser = argparse.ArgumentParser(description='Run disk scheduling simulations')
parser.add_argument('--requests', nargs='+', type=int, required=True)
parser.add_argument('--head', type=int, required=True)
parser.add_argument('--disk-size', type=int, default=None)
parser.add_argument('--direction', type=str, choices=['up', 'down'], default='up')
parser.add_argument('--visualize', action='store_true')
args = parser.parse_args()


if __name__ == '__main__':
sim = DiskScheduler(args.requests, args.head, args.disk_size)
results = sim.simulate_all(visualize=False, direction=args.direction)
for alg, (order, total, avg, moves) in results.items():
print(f"\n{alg}:")
print(" Service order:", order)
print(" Total head movement:", total)
if args.visualize:
plot_results(args.head, results)
