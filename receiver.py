# ESP32 Receiver Simulation

import serial

PORT = "/dev/pts/4"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

print("[ESP32] Listening on UART...")

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print(f"[RAW] {line}")

    if not (line.startswith("<STX>") and line.endswith("<ETX>")):
        print("[ERROR] Invalid packet framing")
        continue

    payload = line.replace("<STX>|", "").replace("|<ETX>", "")
    fields = payload.split("|")

    if len(fields) != 3:
        print("[ERROR] Invalid field count")
        continue

    obj_class, confidence, area = fields

    confidence = float(confidence)
    area = int(area)

    # ---- Decision logic ----
    if obj_class == "person" and confidence > 0.7 and area > 12000:
        print("[ACTION] STOP triggered")
    else:
        print("[ACTION] No action")
