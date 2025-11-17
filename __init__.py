import argparse
import sys
from pathlib import Path


try:
from disk_scheduler import DiskScheduler
except Exception as e:
print("Error importing DiskScheduler from disk_scheduler.py:", e)
print("Make sure disk_scheduler.py is in the same directory and its class constructor is defined as __init__(...) and not _init_.")
sys.exit(1)


AVAILABLE_ALGS = ["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"]