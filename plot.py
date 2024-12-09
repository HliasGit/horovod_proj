import matplotlib.pyplot as plt

# Data from results
gpus = [4, 8, 12, 16]  # Number of GPUs corresponding to 1, 2, 3, and 4 nodes
time = [8 + 0.939 + 0.937 + 0.938, 6 + 0.522 + 0.5125 + 0.523 , 5 + 0.410 + 0.410 +0.359, 5 + 0.281 + 0.322 + 0.280]  # Approximation based on epoch time in results
losses = [1.6958, 1.6597, 1.8205, 1.6534]
accuracy = [0.4271, 0.4426, 0.3927, 0.4396]

# Plot time per epoch
plt.figure(figsize=(10, 6))
plt.plot(gpus, time, marker='o', label='Time (4 epochs)')
plt.title('Strong Scalability: Time vs GPUs')
plt.xlabel('Number of GPUs')
plt.ylabel('Time (4 epochs)')
plt.xticks(gpus)  # Only show GPU values on the x-axis
plt.grid(True)
plt.legend()
plt.show()

# Plot loss and accuracy
plt.figure(figsize=(10, 6))
plt.plot(gpus, losses, marker='o', label='Loss', color='red')
plt.plot(gpus, accuracy, marker='o', label='Accuracy', color='blue')
plt.title('Loss and Accuracy vs GPUs')
plt.xlabel('Number of GPUs')
plt.ylabel('Metrics')
plt.xticks(gpus)  # Only show GPU values on the x-axis
plt.grid(True)
plt.legend()
plt.show()
