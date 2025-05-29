import re
import matplotlib.pyplot as plt
import os

def parse_traceroute(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return []

    with open(file_path, 'r') as f:
        lines = f.readlines()

    hops = []
    for line in lines:
        match = re.findall(r'(\d+\.\d+)\s*ms', line)
        if match:
            avg_latency = sum(map(float, match)) / len(match)
            hops.append(avg_latency)
    return hops

def plot_latency(hops, label):
    if not hops:
        print("No latency data to plot.")
        return

    plt.plot(range(1, len(hops)+1), hops, marker='o', label=label)
    plt.xlabel("Hop Number")
    plt.ylabel("Latency (ms)")
    plt.title("Tunnel Latency Analysis")
    plt.grid(True)

if __name__ == "__main__":
    print("Hey! Welcome to Protocol Latency Analyzer")

    # Ask user for file path
    file_path = input("Enter path to traceroute output file: ").strip()

    # Ask user for label
    label = input("Enter label for the plot (e.g., 'GRE Tunnel'): ").strip()

    # Parse and plot
    hops = parse_traceroute(file_path)
    plot_latency(hops, label)

    if hops:
        # Create output directory if not exists
        os.makedirs("plots", exist_ok=True)
        output_file = "plots/latency_plot.png"
        plt.legend()
        plt.savefig(output_file)
        plt.show()
        print(f"Plot saved as: {output_file}")
