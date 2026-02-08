# Jetson Transmitter Simulation

import serial
import time

PORT = "/dev/pts/5"
BAUD = 115200

ser = serial.Serial(PORT, BAUD)

def send_packet(obj, conf, area):
    packet = f"<STX>|{obj}|{conf:.2f}|{area}|<ETX>\n"
    ser.write(packet.encode())
    print(f"[TX] {packet.strip()}")

# Simulated detection stream
test_data = [
    ("person", 0.85, 18000),
    ("person", 0.60, 20000),
    ("cat", 0.90, 30000),
    ("person", 0.92, 9000),
]

for obj, conf, area in test_data:
    send_packet(obj, conf, area)
    time.sleep(1)
