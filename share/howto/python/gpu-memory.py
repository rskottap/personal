import torch

# Define the memory threshold in bytes (15 GB in this example)
threshold_bytes = 15 * 1024**3  # 15 GB

if torch.cuda.is_available():
    total_memory = torch.cuda.get_device_properties(0).total_memory
    reserved_memory = torch.cuda.memory_reserved(0)
    available_memory = total_memory - reserved_memory

    if available_memory > threshold_bytes:
        print(f"Enough GPU memory available: {available_memory / (1024**3):.2f} GB")
    else:
        print(f"Not enough GPU memory available: {available_memory / (1024**3):.2f} GB")
else:
    print("No GPU found.")

