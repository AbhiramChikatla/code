class Process:
    def __init__(self, pid, arrival_time, burst_time):  # Corrected __init__
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def find_waiting_time(processes):
    waiting_time = [0] * len(processes)
    for i in range(1, len(processes)):
        waiting_time[i] = (processes[i - 1].burst_time + waiting_time[i - 1])
    return waiting_time

def find_turnaround_time(processes, waiting_time):
    turnaround_time = [0] * len(processes)
    for i in range(len(processes)):
        turnaround_time[i] = (processes[i].burst_time + waiting_time[i])
    return turnaround_time

def fcfs_scheduling(processes):
    waiting_time = find_waiting_time(processes)
    turnaround_time = find_turnaround_time(processes, waiting_time)

    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(processes):
        print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Example usage
if __name__ == "__main__":  # Corrected __name__ and __main__
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 8),
        Process(4, 3, 6)
    ]
    
    fcfs_scheduling(processes)
