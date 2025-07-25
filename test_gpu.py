import tensorflow as tf
import time

# Enable device placement logging
tf.debugging.set_log_device_placement(True)

# Create large random tensors
a = tf.random.normal([30000, 3000])
b = tf.random.normal([3000, 4000])

print("Starting heavy GPU computation...")

start = time.time()

for i in range(10):
    c = tf.matmul(a, b)
    # To make sure computation runs, fetch result as numpy (forces evaluation)
    _ = c.numpy()
    print(f"Iteration {i+1} done")

end = time.time()

print(f"Total time for 20 large matmuls: {end - start:.2f} seconds")
