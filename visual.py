# visual.py
"""
Visualization utilities for Disk Scheduling Simulator.
This module plots the movement of the disk head for each algorithm.
"""

import matplotlib.pyplot as plt

def plot_results(head, results, show=True):
    """
    Plot head movement for all algorithms.

    Parameters:
    - head: starting head position
    - results: dictionary produced by simulate_all()
    - show: whether to display the plot (True) or just return the figure (False)
    """
    n_plots = len(results)
    fig, axes = plt.subplots(n_plots, 1, figsize=(8, 2.2 * n_plots), sharex=False)

    if n_plots == 1:
        axes = [axes]

    for ax, (alg, (order, total, avg, moves)) in zip(axes, results.items()):
        # Build head-position timeline
        positions = [head] + order
        ax.step(range(len(positions)), positions, where="post")

        # Scatter points
        ax.scatter(range(len(positions)), positions, s=12)

        ax.set_title(f"{alg} | Total = {total}, Avg = {avg:.2f}")
        ax.set_ylabel("Track")
        ax.grid(True, linestyle="--", linewidth=0.5)

    axes[-1].set_xlabel("Step")

    plt.tight_layout()
    if show:
        plt.show()

    return fig
