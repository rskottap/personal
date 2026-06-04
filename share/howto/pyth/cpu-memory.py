import psutil

# Define the memory threshold in bytes (15 GB in this example)
threshold_bytes = 15 * 1024**3  # 15 GB

# Get the available memory
available_memory = psutil.virtual_memory().available

if available_memory > threshold_bytes:
    print(f"Enough memory available: {available_memory / (1024**3):.2f} GB")
else:
    print(f"Not enough memory available: {available_memory / (1024**3):.2f} GB")

