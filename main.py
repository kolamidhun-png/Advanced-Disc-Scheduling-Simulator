# main.py
from disk_scheduler import DiskScheduler

def to_int_list(text):
    return list(map(int, text.replace(",", " ").split()))

def main():
    print("\n--- Disk Scheduling Simulator ---")

    req = input("Enter disk requests: ").strip()
    requests = to_int_list(req)

    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter total disk size: "))
    direction = input("Direction (up/down): ").lower()
    visualize = input("Enable visualization? (y/n): ").lower() == "y"

    sim = DiskScheduler(requests=requests, head=head, disk_size=disk_size)
    results = sim.simulate_all(visualize=visualize, direction=direction)

    print("\n--- RESULTS ---")
    for alg, (order, total, avg, moves) in results.items():
        print(f"\n{alg}:")
        print(" Order:", order)
        print(" Total Movement:", total)
        print(" Avg Seek:", round(avg, 2))

if __name__ == "__main__":
    main()
