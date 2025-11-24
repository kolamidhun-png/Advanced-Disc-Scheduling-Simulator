# main.py
from disk_scheduler import DiskScheduler

def get_int_list(prompt):
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                return []
            parts = raw.replace(",", " ").split()
            return [int(x) for x in parts]
        except ValueError:
            print("Invalid input! Please enter integers separated by space or comma.")

def main():
    print("\n===== Advanced Disk Scheduling Simulator =====")

    # Input request queue
    requests = get_int_list("Enter disk requests (e.g., 95 180 34 119 10 100 62 198): ")
    if not requests:
        print("No requests entered. Exiting.")
        return

    # Input head position
    while True:
        try:
            head = int(input("Enter initial head position: "))
            break
        except ValueError:
            print("Invalid number!")

    # Input disk size
    while True:
        try:
            disk_size = int(input("Enter total disk size (e.g., 200): "))
            if disk_size <= 0:
                print("Disk size must be positive.")
                continue
            break
        except ValueError:
            print("Invalid number!")

    # Input direction
    while True:
        direction = input("Enter initial direction ('up' or 'down'): ").strip().lower()
        if direction in ("up", "down"):
            break
        print("Invalid direction! Enter 'up' or 'down'.")

    # Visualize graphs?
    vis = input("Do you want visualization? (y/n): ").strip().lower()
    visualize = True if vis == "y" else False

    # Create simulator
    sim = DiskScheduler(requests=requests, head=head, disk_size=disk_size)

    # Run all simulations
    results = sim.simulate_all(visualize=visualize, direction=direction)

    print("\n===== RESULTS =====")
    for alg, (order, total, avg, moves) in results.items():
        print(f"\n{alg}:")
        print(" Service Order      :", order)
        print(" Total Head Movement:", total)
        print(" Average Per Request:", round(avg, 2))
        print(" Per-step Movements :", moves)

    print("\nSimulation complete!\n")

if __name__ == "__main__":
    main()
