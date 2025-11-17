import matplotlib.pyplot as plt




def plot_results(head: int, results: dict):
"""Plot all algorithm sequences. `results` maps name -> (order, total, avg, moves)."""
n = len(results)
fig, axes = plt.subplots(n, 1, figsize=(10, 2.2 * n))
if n == 1:
axes = [axes]
for ax, (name, (order, total, avg, moves)) in zip(axes, results.items()):
pos = [head] + list(order)
ax.step(range(len(pos)), pos, where='post')
ax.scatter(range(len(pos)), pos, s=12)
ax.set_ylabel('Track')
ax.set_title(f"{name} — total={total} avg={avg:.2f}")
ax.grid(True, linestyle=':', linewidth=0.5)
axes[-1].set_xlabel('Sequence step (0=start)')
plt.tight_layout()
plt.show()
