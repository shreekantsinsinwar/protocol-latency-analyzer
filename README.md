# Protocol Latency Analyzer

This tool visualizes hop-by-hop latency across IPSec and GRE tunnels using traceroute output.

## What It Does

- Parses traceroute data
- Extracts latency per hop
- Plots tunnel performance comparison

## How to Use

1. Place traceroute logs in `traceroute_samples/`
2. Run `analyzer.py`
3. View/save graphs from `plots/`

## Future Additions (Coming Soon)

- Support for JSON/Nmap trace formats
- Alerts for hop spikes
- Live monitoring from remote endpoints

---

**Built for real-world tunnel behavior analysis.** Inspired by protocol research and secure traffic steering studies.
