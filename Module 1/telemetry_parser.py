packet = input("Enter telemetry packet: ")
category = packet[0:4].upper()
raw_seconds = int(packet[5:9])
minutes = raw_seconds // 60
seconds = raw_seconds % 60
is_long_session = minutes > 1
print(f"Category: {category}")
print(f"Time: {minutes}m {seconds}s")
print(f"Long session: {is_long_session}")