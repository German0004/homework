is_ready = True

# Те саме, що й у попередньому прикладі, але використовуємо умовний вираз замість умовного оператора
state_msg = 'Ready' if is_ready else 'Not ready yet'
print(state_msg)
