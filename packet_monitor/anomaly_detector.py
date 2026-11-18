from scapy.all import sniff, IP, TCP, UDP, ICMP

print("=" * 50)
print("        NETWORK PACKET MONITOR")
print("=" * 50)
print("Monitoring packets...")
print("Press CTRL+C to stop.")
print()

def packet_callback(packet):

    if IP in packet:

        src = packet[IP].src
        dst = packet[IP].dst

        if TCP in packet:
            print(f"[TCP]  {src} -> {dst} "
                  f"Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"[UDP]  {src} -> {dst} "
                  f"Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print(f"[ICMP] {src} -> {dst}")

sniff(prn=packet_callback, store=False)
