
import socket

target = "127.0.0.1"
ports = [22, 80, 443, 3000, 8080]

print(" Local Port Scanner")
print(f"target: {target}")
print()

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    sock.close()

print()
print("scan completed")



