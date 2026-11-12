primary_server = 8000
fallback_server = primary_server
print(f"Primary server id: {id(primary_server)}")
print(f"Fallback server id: {id(fallback_server)}")
print(f"Same object: {id(primary_server) == id(fallback_server)}")