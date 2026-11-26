session_xp = []
start_id = id(session_xp)
session_xp.append(50)
session_xp.append(120)
session_xp.append(30)
print(f"Session XP: {session_xp}")
print(f"Same object: {start_id == id(session_xp)}")