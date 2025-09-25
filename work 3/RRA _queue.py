# RRA Queue: 9 citizens
rra_queue = ["Citizen 1", "Citizen 2", "Citizen 3", "Citizen 4", "Citizen 5", 
             "Citizen 6", "Citizen 7", "Citizen 8", "Citizen 9"]
print("RRA Queue:")
print("Initial queue:", rra_queue)

# Serve 4 citizens by removing them from the front (FIFO)
rra_queue.pop(0)  # Remove Citizen 1
rra_queue.pop(0)  # Remove Citizen 2
rra_queue.pop(0)  # Remove Citizen 3
rra_queue.pop(0)  # Remove Citizen 4

print("Queue after serving 4 people:", rra_queue)
print("Next to be served:", rra_queue[0])