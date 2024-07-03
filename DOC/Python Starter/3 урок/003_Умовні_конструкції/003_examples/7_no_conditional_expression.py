is_ready = True

# Привласнюємо значення змінної залежно від умови
if is_ready:
    state_msg = 'Ready'
else:
    state_msg = 'Not ready yet'

print(state_msg)
