import re
import matplotlib.pyplot as plt

def parse_traceroute(file_path):
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
    plt.plot(range(1, len(hops)+1), hops, marker='o', label=label)
    plt.xlabel("Hop Number")
    plt.ylabel("Latency (ms)")
    plt.title("Tunnel Latency Analysis")
    plt.grid(True)

if __name__ == "__main__":
    gre_latency = parse_traceroute("traceroute_samples/tunnel_trace_gre.txt")
    ipsec_latency = parse_traceroute("traceroute_samples/tunnel_trace_linux.txt")

    plot_latency(gre_latency, label="GRE Tunnel")
    plot_latency(ipsec_latency, label="IPSec Tunnel")

    plt.legend()
    plt.savefig("plots/latency_plot.png")
    plt.show()
