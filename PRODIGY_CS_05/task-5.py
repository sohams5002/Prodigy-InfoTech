from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

class NetworkAnalyzer:
    def __init__(self):
        self.packet_count = 0

    def packet_callback(self, packet):
        """Processes each captured packet in real-time."""
        if IP in packet:
            self.packet_count += 1
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto = packet[IP].proto
            
            # Map protocol numbers to names
            protocol_name = "Other"
            if packet.haslayer(TCP): protocol_name = "TCP"
            elif packet.haslayer(UDP): protocol_name = "UDP"
            elif packet.haslayer(ICMP): protocol_name = "ICMP"

            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] #{self.packet_count} | {protocol_name} | {src_ip} -> {dst_ip}")

            # Extract Payload Data
            if packet.haslayer(Raw):
                payload = packet[Raw].load
                # Professional Tip: Only print printable characters to avoid terminal corruption
                try:
                    decoded_payload = payload.decode('utf-8', 'ignore')
                    if decoded_payload.strip():
                        print(f"   Payload: {decoded_payload[:50]}...")
                except Exception:
                    print(f"   Payload: [Binary Data - {len(payload)} bytes]")

    def start(self, interface=None):
        print(f"[*] Starting Packet Sniffer on {interface if interface else 'default interface'}...")
        print("[*] Press Ctrl+C to stop.")
        # store=0 is critical for real-world use to prevent memory leaks
        sniff(iface=interface, prn=self.packet_callback, store=0)

# --- Execution ---
if __name__ == "__main__":
    analyzer = NetworkAnalyzer()
    # You can specify a filter like: filter="tcp port 80"
    try:
        analyzer.start()
    except KeyboardInterrupt:
        print("\n[!] Sniffer stopped.")