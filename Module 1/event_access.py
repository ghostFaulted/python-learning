player_level = 12
has_invite = False
is_staff = True
meets_requirements = player_level > 10 and has_invite
can_enter = meets_requirements or is_staff
print(f"Meets requirements: {meets_requirements}")
print(f"Can enter: {can_enter}")