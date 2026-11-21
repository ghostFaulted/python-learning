latency = 200
if latency > 150:
    print("Critical")
elif latency > 50:
    print("Warning")
else:
    print("OK")