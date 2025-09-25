# Stack simulation for MoMo transaction
momo_stack = []

# Push transaction steps
momo_stack.append("PIN")
momo_stack.append("Amount")
momo_stack.append("Confirm")

# Undo 2 steps (pop twice)
momo_stack.pop()
momo_stack.pop()

# Print remaining steps
print("Remaining MoMo step:", momo_stack)
