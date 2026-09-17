import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

import pyshark

cap = pyshark.FileCapture("data/raw_captures/chatgpt_shortqa_01.pcapng")

count = 0
for packet in cap:
    count += 1
    if count <= 3:
        print(f"Packet {count}: length={packet.length}, protocol={packet.highest_layer}")

print(f"\nTotal packets read: {count}")
cap.close()