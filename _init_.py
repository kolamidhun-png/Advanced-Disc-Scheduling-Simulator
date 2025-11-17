"""disk_scheduler package entry points"""
from .algorithms import DiskScheduler
from .plotter import plot_results


__all__ = ["DiskScheduler", "plot_results"]
